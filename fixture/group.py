import time
from model.group_info import Group
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.group_cache = None
        wd = self.app.wd
        self.wait = WebDriverWait(wd, 5, poll_frequency=0.1)

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page with check
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
        else:
            pass  # пропускаем шаг если уже на груп.пхп

    def new_group_button(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
        what_to_wait = wd.find_element(By.XPATH, "(//input[@name='edit'])[1]")
        self.wait.until(EC.visibility_of(what_to_wait))
        wd.find_element_by_name("new").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.group_cache = None
        # self.creating_complete_message()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.group_cache = None
        # self.editing_complete_message()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        self.group_cache = None
        # self.deletion_complete_message()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        self.group_cache = None
        # self.deletion_complete_message()

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        self.group_cache = None
        # self.deletion_complete_message()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # wd.find_element_by_xpath('//*[@class="group"]//*[@value="%s"]' % str(id)).click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_xpath("(//input[@name='edit'])[1]").click()

    def edit_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_xpath("(//input[@name='edit'])[1]").click()

    def fill_form_with_check(self, group):
        # использовать вместе с param_check_with_name_loc
        locator_name = "group_name"
        locator_header = "group_header"
        locator_footer = "group_footer"
        self.param_check_with_name_loc(group.name, locator_name)
        self.param_check_with_name_loc(group.header, locator_header)
        self.param_check_with_name_loc(group.footer, locator_footer)

    def param_check_with_name_loc(self, param, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(param)
        else:  # Можно убрать елсе блок. Оставил что бы смотреть за шагами
            wd.find_element_by_name(locator).click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def is_it_group_form(self):
        wd = self.app.wd
        self.open_groups_page()
        return wd.find_elements_by_name('submit') > 0

    def creating_complete_message(self):
        wd = self.app.wd
        text = "A new group has been entered into the address book.\nreturn to the group page"
        locator = wd.find_element_by_xpath('//*[@id="content"]/div').text
        if locator == text:
            self.group_cache = None
            print("Группа создана, текст ОК!")
            return True
        else:
            self.group_cache = None
            print("В тексте сообщения об успешном создании группы - ошибка")
            return False

    def editing_complete_message(self):
        wd = self.app.wd
        text = "Group record has been updated.\nreturn to the group page"
        locator = wd.find_element_by_xpath('//*[@id="content"]/div').text
        if locator == text:
            print("Группа изменена, текст ОК!")
            return True
        else:
            print("В тексте сообщения об успешном изменении группы - ошибка")
            return False

    def deletion_complete_message(self):
        wd = self.app.wd
        text = "Group has been removed.\nreturn to the group page"
        locator = wd.find_element_by_xpath('//*[@id="content"]/div').text
        if locator == text:
            self.group_cache = None
            print("Группа удалена, текст ОК!")
            return True
        else:
            self.group_cache = None
            print("В тексте сообщения об успешном удалении группы - ошибка")
            return False

    # Вызывать каждый раз когда есть проверка на кол-во групп, что бы создать группу только для теста
    # Просто создание тестовой группы, без всяких проверок
    def add_empty_group(self, amount):
        if self.count() <= amount:
            count = self.count()
            while count < amount:      # создаём пока не достигнем нужного числа
                count += 1
                self.open_groups_page()
                self.new_group_button()
                self.fill_form_with_check(Group(name="", header="", footer=""))
                self.submit()
                self.open_groups_page()

    def add_group(self, amount):
        if self.count() < amount:
            count = self.count()
            while count < amount:      # создаём пока не достигнем нужного числа
                count += 1
                text = str(count) + ' Это порядковый номер'
                self.open_groups_page()
                self.new_group_button()
                self.fill_form_with_check(Group(name=text, header="Какой-то хедер", footer="Какой-то футер"))
                self.submit()
                self.open_groups_page()

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return self.group_cache

    # wtf - what to find
    def get_group_index_by_name(self, name):
        wd = self.app.wd
        n = 1
        m = self.count()
        # print(m)
        while n <= m:
            locator = f'//*[@class="group"][{n}]'
            if wd.find_element_by_xpath(locator).text == name:
                # print("индекс", n-1)
                # n += 1
                return n - 1
            else:  # раскомментировать для отладки и ремонта
                # print(n-1, n, "not_find")
                n += 1

    def get_group_id_by_name(self, name):
        wd = self.app.wd
        n = 1
        m = self.count()
        # print(m)
        while n <= m:
            locator = f'//*[@class="group"][{n}]'
            locator_value = f'//*[@class="group"][{n}]//input'
            if wd.find_element_by_xpath(locator).text == name:
                # print(wd.find_element_by_xpath(locator_value).get_attribute('value'))
                # n += 1
                return wd.find_element_by_xpath(locator_value).get_attribute('value')

            else:
                # print(wd.find_element_by_xpath(locator).text, n, "not_find")
                n += 1
