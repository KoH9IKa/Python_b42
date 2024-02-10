import time
import re
from model.contact_info import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None
        # contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        # open groups page with check
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()
        else:
            pass  # если уже на нужной странице - пропускаем шаг

    def add_next_contact(self):  # проверка на страницу не нужна так как попасть на страницу, где кнопка -
        wd = self.app.wd  # можно только через создание группы
        # return to form for add next address
        wd.find_element_by_xpath("//a[normalize-space()='add next']").click()

    def add_new_contact(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()

    def press_top_enter_button(self):
        wd = self.app.wd
        # top "enter" button
        wd.find_element_by_xpath("(//input[@name='submit'])[1]").click()
        self.contact_cache = None

    def press_bottom_enter_button(self):
        wd = self.app.wd
        # bottom "enter" button
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def sort_by_last_name(self):
        wd = self.app.wd
        # call once to asc, call twice to desc
        wd.find_element_by_xpath("//a[@title='Sort on “Last name”']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_checkbox_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def select_checkbox_by_index(self, index):
        wd = self.app.wd
        # wd.find_elements_by_name("selected[]")[index].click()  # работает, но я ему не доверяю
        # еще 1 вариант рабочий
        index += 2
        locator = f'//tr[{index}]//td[1]//input[@type="checkbox"]'
        wd.find_element_by_xpath(locator).click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        index += 2
        locator = f'//tr[{index}]//td[8]//a//img'
        wd.find_element_by_xpath(locator).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        index += 2
        locator = f'//tr[{index}]//td[7]//a//img'
        wd.find_element_by_xpath(locator).click()

    def press_top_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[1]").click()
        self.contact_cache = None

    def press_bot_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def select_all_checkbox(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="MassCB"]').click()

    def delete_button_in_table(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def fill_form_with_check(self, contact):
        # Идёт в комплекте с (input_check_with_xpath + day_and_month_selector_check). Там где данные не трогаем -
        # ставим None, если стоит None то поле только кликается, что бы успеть видеть на каком поле находится тест
        locator_first_name = "//input[@name='firstname']"
        locator_mid_name = "//input[@name='middlename']"
        locator_last_name = "//input[@name='lastname']"
        locator_nick_name = "//input[@name='nickname']"
        locator_title = "//input[@name='title']"
        locator_company = "//input[@name='company']"
        locator_address = "//textarea[@name='address']"
        locator_home_phone = "//input[@name='home']"
        locator_mob_phone = "//input[@name='mobile']"
        locator_work_phone = "//input[@name='work']"
        locator_fax = "//input[@name='fax']"
        locator_email = "//input[@name='email']"
        locator_email2 = "//input[@name='email2']"
        locator_email3 = "//input[@name='email3']"
        locator_homepage_url = "//input[@name='homepage']"
        locator_bday_selector = "//select[@name='bday']"  # то где! выбираем
        bday_locator = f'select[name="bday"] > option[value="{contact.bday}"]'  # то что! выбираем
        locator_bmonth_selector = "//select[@name='bmonth']"
        bmonth_locator = f'select[name="bmonth"] > option[value="{contact.bmonth}"]'
        locator_byear = "(//input[@name='byear'])[1]"
        locator_aday_selector = "//select[@name='aday']"
        aday_locator = f'select[name="aday"] > option[value="{contact.aday}"]'
        locator_amonth_selector = "//select[@name='amonth']"
        amonth_locator = f'select[name="amonth"] > option[value="{contact.amonth}"]'
        locator_ayear = "(//input[@name='ayear'])[1]"
        self.input_check_with_xpath(contact.first_name, locator_first_name)
        self.input_check_with_xpath(contact.mid_name, locator_mid_name)
        self.input_check_with_xpath(contact.last_name, locator_last_name)
        self.input_check_with_xpath(contact.nick_name, locator_nick_name)
        self.input_check_with_xpath(contact.company, locator_company)
        self.input_check_with_xpath(contact.title, locator_title)
        self.input_check_with_xpath(contact.address, locator_address)
        self.input_check_with_xpath(contact.home_tel, locator_home_phone)
        self.input_check_with_xpath(contact.mob_tel, locator_mob_phone)
        self.input_check_with_xpath(contact.work_tel, locator_work_phone)
        self.input_check_with_xpath(contact.fax_tel, locator_fax)
        self.input_check_with_xpath(contact.email, locator_email)
        self.input_check_with_xpath(contact.email2, locator_email2)
        self.input_check_with_xpath(contact.email3, locator_email3)
        self.input_check_with_xpath(contact.homepage_url, locator_homepage_url)
        # Birth Day
        self.day_and_month_selector_check(contact.bday, locator_bday_selector, bday_locator)
        self.day_and_month_selector_check(contact.bmonth, locator_bmonth_selector, bmonth_locator)
        self.input_check_with_xpath(contact.byear, locator_byear)
        # Anni Day
        self.day_and_month_selector_check(contact.aday, locator_aday_selector, aday_locator)
        self.day_and_month_selector_check(contact.amonth, locator_amonth_selector, amonth_locator)
        self.input_check_with_xpath(contact.ayear, locator_ayear)

    def input_check_with_xpath(self, param, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_xpath(locator).click()
            wd.find_element_by_xpath(locator).clear()
            wd.find_element_by_xpath(locator).send_keys(param)
        else:  # Можно убрать елсе блок. Оставил что бы смотреть за шагами
            wd.find_element_by_xpath(locator).click()

    def day_and_month_selector_check(self, param, select, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_xpath(select).click()
            wd.find_element_by_css_selector(locator).click()
        else:  # Можно убрать елсе блок. Оставил что бы смотреть за шагами
            wd.find_element_by_xpath(select).click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def add_default_empty_contact(self, amount):
        if self.count() < amount:
            count = self.count()
            while count < amount:  # создаём пока не достигнем нужного числа
                count += 1
                self.add_new_contact()
                self.fill_form_with_check(Contact())
                self.press_top_enter_button()
                self.contact_cache = None
                self.open_contacts_page()

    def add_default_filled_contact(self, amount):  # в amount передаём кол-во записей которые нам нужны
        if self.count() < amount:
            count = self.count()
            while count < amount:  # создаём пока не достигнем нужного числа
                count += 1
                # text = f'{count} - это порядковый номер'
                text = f'{count} Фамилия'
                self.add_new_contact()
                self.fill_form_with_check(Contact(first_name=text,  # пока что для отслеживания - отправляем номер
                                                  mid_name="Тестовый",
                                                  last_name="Имя",
                                                  nick_name="Который",
                                                  title="Имеет",
                                                  photo="",
                                                  company='ОООООООЧень обычные',
                                                  address="7777777, строки с данными",
                                                  mob_tel="+7(123)456 78 98",
                                                  work_tel="+7(123)456 78 99",
                                                  home_tel="+7(123)456 78 10",
                                                  fax_tel="+7(123)456 78 11",
                                                  email="test@mail.ru",
                                                  email2="test2@mail.ru",
                                                  email3="test3@mail.ru",
                                                  homepage_url="https:\\www.homepage2.com",
                                                  bday="5", bmonth="5", byear="2023",  # валидный дд мм
                                                  aday="5", amonth="5", ayear="2003"))  # валидный дд мм
                self.press_top_enter_button()
                self.contact_cache = None
                self.open_contacts_page()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for elem in wd.find_elements_by_xpath('//*[@id="maintable"]//tbody//tr[@name="entry"]'):
                id = elem.find_element_by_xpath('.//td[1]//input').get_attribute("value")
                last_name = elem.find_element_by_xpath('.//td[2]').text
                first_name = elem.find_element_by_xpath('.//td[3]').text
                address = elem.find_element_by_xpath('.//td[4]').text
                all_emails = elem.find_element_by_xpath('.//td[5]').text
                all_phones = elem.find_element_by_xpath('.//td[6]').text
                self.contact_cache.append(
                        Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                                all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
            # print(self.contact_cache)
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        mob_tel = self.clear_phone(wd.find_element_by_name('mobile').get_attribute('value'))
        work_tel = self.clear_phone(wd.find_element_by_name('work').get_attribute('value'))
        home_tel = self.clear_phone(wd.find_element_by_name('home').get_attribute('value'))
        fax_tel = self.clear_phone(wd.find_element_by_name('fax').get_attribute('value'))
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(id=id, first_name=first_name, last_name=last_name, address=address,
                       mob_tel=mob_tel, work_tel=work_tel, home_tel=home_tel, fax_tel=fax_tel,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = self.clear_phone(re.search("H: (.*)", text).group(1))
        mob_tel = self.clear_phone(re.search("M: (.*)", text).group(1))
        work_tel = self.clear_phone(re.search("W: (.*)", text).group(1))
        fax_tel = self.clear_phone(re.search("F: (.*)", text).group(1))
        return Contact(mob_tel=mob_tel, work_tel=work_tel, home_tel=home_tel, fax_tel=fax_tel)

    def clear_phone(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        # Соединяем телефоны в вид тел1\nтел2\nтел3 для сравнения с ячейкой где всё в 3 строки идёт
        return "\n".join(filter(lambda x: x != "",  # не пустая строка
                                map(lambda x: self.clear_phone(x),  # очищаем телефон от хлама
                                    filter(lambda x: x is not None,  # телефон не None
                                           [contact.home_tel,
                                            contact.mob_tel,
                                            contact.work_tel
                                            # contact.fax_tel  #его нет на главной
                                            ]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",  # не пустая строка
                                filter(lambda x: x is not None,  # телефон не None
                                       [contact.email, contact.email2, contact.email3])))
