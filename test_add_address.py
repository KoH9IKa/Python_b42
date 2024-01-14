# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact_info import Name, Other, Address, Phone, Email, Date


class TestAddGroup(unittest.TestCase):
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

    def fill_address_form(self, wd, name, other, address, phone, email, date):
        # fill name/midname/lastname/nickname
        wd.find_element_by_xpath("//input[@name='firstname']").click()
        wd.find_element_by_xpath("//input[@name='firstname']").clear()
        wd.find_element_by_xpath("//input[@name='firstname']").send_keys(name.first_name)
        wd.find_element_by_xpath("//input[@name='middlename']").click()
        wd.find_element_by_xpath("//input[@name='middlename']").clear()
        wd.find_element_by_xpath("//input[@name='middlename']").send_keys(name.mid_name)
        wd.find_element_by_xpath("//input[@name='lastname']").click()
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys(name.last_name)
        wd.find_element_by_xpath("//input[@name='nickname']").click()
        wd.find_element_by_xpath("//input[@name='nickname']").clear()
        wd.find_element_by_xpath("//input[@name='nickname']").send_keys(name.nick_name)
        # fill other information
        wd.find_element_by_xpath("//input[@name='title']").click()
        wd.find_element_by_xpath("//input[@name='title']").clear()
        wd.find_element_by_xpath("//input[@name='title']").send_keys(other.title)
        wd.find_element_by_xpath("//input[@name='company']").click()
        wd.find_element_by_xpath("//input[@name='company']").clear()
        wd.find_element_by_xpath("//input[@name='company']").send_keys(other.company)
        # fill address field
        wd.find_element_by_xpath("//textarea[@name='address']").click()
        wd.find_element_by_xpath("//textarea[@name='address']").clear()
        wd.find_element_by_xpath("//textarea[@name='address']").send_keys(address.address)
        # fill phones & fax
        wd.find_element_by_xpath("//input[@name='home']").click()
        wd.find_element_by_xpath("//input[@name='home']").clear()
        wd.find_element_by_xpath("//input[@name='home']").send_keys(phone.home_tel)
        wd.find_element_by_xpath("//input[@name='mobile']").click()
        wd.find_element_by_xpath("//input[@name='mobile']").clear()
        wd.find_element_by_xpath("//input[@name='mobile']").send_keys(phone.mob_tel)
        wd.find_element_by_xpath("//input[@name='work']").click()
        wd.find_element_by_xpath("//input[@name='work']").clear()
        wd.find_element_by_xpath("//input[@name='work']").send_keys(phone.work_tel)
        wd.find_element_by_xpath("//input[@name='fax']").click()
        wd.find_element_by_xpath("//input[@name='fax']").clear()
        wd.find_element_by_xpath("//input[@name='fax']").send_keys(phone.fax_tel)
        # fill email & homepage url
        wd.find_element_by_xpath("//input[@name='email']").click()
        wd.find_element_by_xpath("//input[@name='email']").clear()
        wd.find_element_by_xpath("//input[@name='email']").send_keys(email.email)
        wd.find_element_by_xpath("//input[@name='email2']").click()
        wd.find_element_by_xpath("//input[@name='email2']").clear()
        wd.find_element_by_xpath("//input[@name='email2']").send_keys(email.email_2)
        wd.find_element_by_xpath("//input[@name='email3']").click()
        wd.find_element_by_xpath("//input[@name='email3']").clear()
        wd.find_element_by_xpath("//input[@name='email3']").send_keys(email.email_3)
        wd.find_element_by_xpath("//input[@name='homepage']").click()
        wd.find_element_by_xpath("//input[@name='homepage']").clear()
        wd.find_element_by_xpath("//input[@name='homepage']").send_keys(email.homepage_url)
        wd.find_element_by_xpath("//input[@name='work']").click()
        wd.find_element_by_xpath("//input[@name='work']").clear()
        wd.find_element_by_xpath("//input[@name='work']").send_keys(phone.work_tel)
        # Born date setting
        wd.find_element_by_xpath("//select[@name='bday']").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form/select[1]/option[10]").click()
        wd.find_element_by_xpath("//select[@name='bmonth']").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form/select[2]/option[6]").click()
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='byear'])[1]").send_keys(date.byear)
        # Anniversary date setting
        wd.find_element_by_xpath("//select[@name='aday']").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form/select[3]/option[10]").click()
        wd.find_element_by_xpath("//select[@name='amonth']").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form/select[4]/option[6]").click()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").send_keys(date.ayear)

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
        self.fill_address_form(wd,
                               Name(first_name="Константин",
                                    mid_name="Андреевич",
                                    last_name="Верченко",
                                    nick_name="Костян"),
                               Other(title="QA Eng.",
                                     photo="",
                                     company='ООО "Мартышка и очки"'),
                               Address(address="298300, г.Васюканск, ул.Из Костылей Строителей, д.404"),
                               Phone(mob_tel="+7(123)456 78 90",
                                     work_tel="+7(123)456 78 91",
                                     home_tel="+7(123)456 78 92",
                                     fax_tel="+7(123)456 78 93"),
                               Email(email="email1@mail.ru",
                                     email_2="email2@mail.ru",
                                     email_3="email3@mail.ru",
                                     homepage_url="https:\\www.homepage.com"),
                               Date(bday="", bmonth=7, byear="1992",
                                    aday="", amonth=7, ayear="2022")
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
        self.fill_address_form(wd,
                               Name(first_name="Валерий",
                                    mid_name="Непомню",
                                    last_name="Меладзе",
                                    nick_name="Я_КРАСИВЫЙ"),
                               Other(title="сингер",
                                     photo="",
                                     company='ООО "Я Продюсер ВИА ГРЫ"'),
                               Address(address="7777777, г.Меладзовское, ул.Певцова, д.3"),
                               Phone(mob_tel="+7(123)456 78 98",
                                     work_tel="+7(123)456 78 99",
                                     home_tel="+7(123)456 78 10",
                                     fax_tel="+7(123)456 78 11"),
                               Email(email="email4@mail.ru",
                                     email_2="email5@mail.ru",
                                     email_3="email6@mail.ru",
                                     homepage_url="https:\\www.homepage2.com"),
                               Date(bday="", bmonth=2, byear="1993",
                                    aday="", amonth=3, ayear="2023")
                               )
        self.press_bottom_enter_button(wd)
        self.return_to_home_page(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
