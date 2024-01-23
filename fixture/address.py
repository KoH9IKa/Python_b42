
class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_next_address(self):
        wd = self.app.wd
        # return to form for add next address
        wd.find_element_by_xpath("//a[normalize-space()='add next']").click()

    def add_new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def press_top_enter_button(self):
        wd = self.app.wd
        # top "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[1]").click()

    def press_bottom_enter_button(self):
        wd = self.app.wd
        # bottom "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def sort_by_last_name(self):
        wd = self.app.wd
        # call once to asc, call twice to desc
        wd.find_element_by_xpath("//a[@title='Sort on “Last name”']").click()

    def delete_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit_first_address_in_table(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@title='Edit'])[1]").click()

    def press_top_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[1]")

    def press_bot_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[2]")

    def edit_or_create_with_check(self, contact):
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
        locator_bday_selector = "//select[@name='bday']"                        # то где! выбираем
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
        return

    def day_and_month_selector_check(self, param, select, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_xpath(select).click()
            wd.find_element_by_css_selector(locator).click()
        else:  # Можно убрать елсе блок. Оставил что бы смотреть за шагами
            wd.find_element_by_xpath(select).click()
        return
