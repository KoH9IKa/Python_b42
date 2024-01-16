# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact_info import Contact


class TestAddNewAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_xpath("//input[@name='user']").click()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").click()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_new_address_form(self, wd):
        # open "new address" page
        wd.find_element_by_link_text("add new").click()

    def fill_address_form(self, wd, contact):
        # fill name/midname/lastname/nickname
        wd.find_element_by_xpath("//input[@name='firstname']").click()
        wd.find_element_by_xpath("//input[@name='firstname']").clear()
        wd.find_element_by_xpath("//input[@name='firstname']").send_keys(contact.first_name)
        wd.find_element_by_xpath("//input[@name='middlename']").click()
        wd.find_element_by_xpath("//input[@name='middlename']").clear()
        wd.find_element_by_xpath("//input[@name='middlename']").send_keys(contact.mid_name)
        wd.find_element_by_xpath("//input[@name='lastname']").click()
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys(contact.last_name)
        wd.find_element_by_xpath("//input[@name='nickname']").click()
        wd.find_element_by_xpath("//input[@name='nickname']").clear()
        wd.find_element_by_xpath("//input[@name='nickname']").send_keys(contact.nick_name)
        # fill other information
        wd.find_element_by_xpath("//input[@name='title']").click()
        wd.find_element_by_xpath("//input[@name='title']").clear()
        wd.find_element_by_xpath("//input[@name='title']").send_keys(contact.title)
        wd.find_element_by_xpath("//input[@name='company']").click()
        wd.find_element_by_xpath("//input[@name='company']").clear()
        wd.find_element_by_xpath("//input[@name='company']").send_keys(contact.company)
        # fill address field
        wd.find_element_by_xpath("//textarea[@name='address']").click()
        wd.find_element_by_xpath("//textarea[@name='address']").clear()
        wd.find_element_by_xpath("//textarea[@name='address']").send_keys(contact.address)
        # fill phones & fax
        wd.find_element_by_xpath("//input[@name='home']").click()
        wd.find_element_by_xpath("//input[@name='home']").clear()
        wd.find_element_by_xpath("//input[@name='home']").send_keys(contact.home_tel)
        wd.find_element_by_xpath("//input[@name='mobile']").click()
        wd.find_element_by_xpath("//input[@name='mobile']").clear()
        wd.find_element_by_xpath("//input[@name='mobile']").send_keys(contact.mob_tel)
        wd.find_element_by_xpath("//input[@name='work']").click()
        wd.find_element_by_xpath("//input[@name='work']").clear()
        wd.find_element_by_xpath("//input[@name='work']").send_keys(contact.work_tel)
        wd.find_element_by_xpath("//input[@name='fax']").click()
        wd.find_element_by_xpath("//input[@name='fax']").clear()
        wd.find_element_by_xpath("//input[@name='fax']").send_keys(contact.fax_tel)
        # fill email & homepage url
        wd.find_element_by_xpath("//input[@name='email']").click()
        wd.find_element_by_xpath("//input[@name='email']").clear()
        wd.find_element_by_xpath("//input[@name='email']").send_keys(contact.email)
        wd.find_element_by_xpath("//input[@name='email2']").click()
        wd.find_element_by_xpath("//input[@name='email2']").clear()
        wd.find_element_by_xpath("//input[@name='email2']").send_keys(contact.email_2)
        wd.find_element_by_xpath("//input[@name='email3']").click()
        wd.find_element_by_xpath("//input[@name='email3']").clear()
        wd.find_element_by_xpath("//input[@name='email3']").send_keys(contact.email_3)
        wd.find_element_by_xpath("//input[@name='homepage']").click()
        wd.find_element_by_xpath("//input[@name='homepage']").clear()
        wd.find_element_by_xpath("//input[@name='homepage']").send_keys(contact.homepage_url)
        wd.find_element_by_xpath("//input[@name='work']").click()
        wd.find_element_by_xpath("//input[@name='work']").clear()
        wd.find_element_by_xpath("//input[@name='work']").send_keys(contact.work_tel)
        # Born date setting
        bday_locator = f'select[name="bday"] > option[value="{contact.bday}"]'
        wd.find_element_by_xpath("//select[@name='bday']").click()
        wd.find_element_by_css_selector(bday_locator).click()
        # Born month setting
        bmonth_locator = f'select[name="bmonth"] > option[value="{contact.bmonth}"]'
        wd.find_element_by_xpath("//select[@name='bmonth']").click()
        wd.find_element_by_css_selector(bmonth_locator).click()
        # Born year setting
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").send_keys(contact.byear)
        # Anniversary date setting
        aday_locator = f'select[name="aday"] > option[value="{contact.aday}"]'
        wd.find_element_by_xpath("//select[@name='aday']").click()
        wd.find_element_by_css_selector(aday_locator).click()
        # Anniversary month setting
        amonth_locator = f'select[name="amonth"] > option[value="{contact.amonth}"]'
        wd.find_element_by_xpath("//select[@name='bmonth']").click()
        wd.find_element_by_css_selector(amonth_locator).click()
        # Anniversary year setting
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").send_keys(contact.ayear)

    def return_to_home_page(self, wd):
        # return to home page
        wd.find_element_by_xpath("//a[normalize-space()='home']").click()

    def add_next_address(self, wd):
        # return to form for add next address
        wd.find_element_by_xpath("//a[normalize-space()='add next']").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def press_top_enter_button(self, wd):
        # top "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[1]").click()

    def press_bottom_enter_button(self, wd):
        # bottom "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def test_add_address_top_but(self):
        # test with top "enter" button
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_address_form(wd)
        # Месяц вводить цифрами от "1" до "12", День от "1" до "31"
        self.fill_address_form(wd,
                               Contact(first_name="Константин",
                                       mid_name="Андреевич",
                                       last_name="Верченко",
                                       nick_name="Костян",
                                       title="QA Eng.",
                                       photo="",
                                       company='ООО "Мартышка и очки"',
                                       address="298300, г.Васюканск, ул.Из Костылей Строителей, д.404",
                                       mob_tel="+7(123)456 78 90",
                                       work_tel="+7(123)456 78 91",
                                       home_tel="+7(123)456 78 92",
                                       fax_tel="+7(123)456 78 93",
                                       email="email1@mail.ru",
                                       email_2="email2@mail.ru",
                                       email_3="email3@mail.ru",
                                       homepage_url="https:\\www.homepage.com",
                                       bday="32", bmonth="33", byear="1995",  # невалидный дд мм
                                       aday="35", amonth="33", ayear="2022")  # невалидный дд мм
                               )
        self.press_top_enter_button(wd)
        self.add_next_address(wd)
        # check that next address link also is working and go to home page
        self.return_to_home_page(wd)
        # and logout
        self.logout(wd)

    def test_add_address_bot_but(self):
        # test with bottom "enter" button
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_address_form(wd)
        # Месяц вводить цифрами от "1" до "12", День от "1" до "31"
        self.fill_address_form(wd,
                               Contact(first_name="Валерий",
                                       mid_name="Непомню",
                                       last_name="Меладзе",
                                       nick_name="Я_КРАСИВЫЙ",
                                       title="сингер",
                                       photo="",
                                       company='ООО "Я Продюсер ВИА ГРЫ"',
                                       address="7777777, г.Меладзовское, ул.Певцова, д.3",
                                       mob_tel="+7(123)456 78 98",
                                       work_tel="+7(123)456 78 99",
                                       home_tel="+7(123)456 78 10",
                                       fax_tel="+7(123)456 78 11",
                                       email="email4@mail.ru",
                                       email_2="email5@mail.ru",
                                       email_3="email6@mail.ru",
                                       homepage_url="https:\\www.homepage2.com",
                                       bday="29", bmonth="1", byear="1993",  # валидный дд мм
                                       aday="1", amonth="12", ayear="2023")  # валидный дд мм
                               )
        self.press_bottom_enter_button(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
