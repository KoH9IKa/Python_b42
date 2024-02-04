import time
from model.group_info import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

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
        wd.find_element_by_name("new").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()

    def edit_first_group_in_table(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
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
            return True
        else:
            print("В тексте сообщения об успешном создании группы - ошибка")
            return False

    def editing_complete_message(self):
        wd = self.app.wd
        text = "Group record has been updated.\nreturn to the group page"
        locator = wd.find_element_by_xpath('//*[@id="content"]/div').text
        if locator == text:
            return True
        else:
            print("В тексте сообщения об успешном изменении группы - ошибка")
            return False

    def deletion_complete_message(self):
        wd = self.app.wd
        text = "Group has been removed.\nreturn to the group page"
        locator = wd.find_element_by_xpath('//*[@id="content"]/div').text
        if locator == text:
            return True
        else:
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

    def get_group_list(self):
        wd = self.app.wd
        groups_list = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups_list.append(Group(name=text, id=id))
        return groups_list

