

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_next_address(self):
        wd = self.app.wd
        # return to form for add next address
        wd.find_element_by_xpath("//a[normalize-space()='add next']").click()

    def add_new_address(self):
        wd = self.app.wd
        # return to form for add next address
        wd.find_element_by_link_text("add new").click()

    def press_top_enter_button(self):
        wd = self.app.wd
        # top "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[1]").click()

    def press_bottom_enter_button(self):
        wd = self.app.wd
        # bottom "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def create(self, contact):
        wd = self.app.wd
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
        wd.find_element_by_xpath("//input[@name='email2']").send_keys(contact.email2)
        wd.find_element_by_xpath("//input[@name='email3']").click()
        wd.find_element_by_xpath("//input[@name='email3']").clear()
        wd.find_element_by_xpath("//input[@name='email3']").send_keys(contact.email3)
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
        wd.find_element_by_xpath("//select[@name='amonth']").click()
        wd.find_element_by_css_selector(amonth_locator).click()
        # Anniversary year setting
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").send_keys(contact.ayear)
        # так как кнопок подтверждения на форме 2 - их сюда пока не помещал

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
        # Можно использовать вместо create так как тут есть проверка. Идёт в комплекте с
        # (input_check_with_xpath + day_and_month_selector_check)
        # В тесте на изменение данных там где данные не трогаем - ставим None, если стоит None то поле только кликается,
        # что бы успеть видеть на каком поле находится тест
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

    # def edit_with_separate_check(self, contact):
    # Рабочий, но очень много строк/
    # тоже самое в edit_with_check + (input_check_with_xpath + day_and_month_selector_check)
    # В тесте на изменение данных там где данные не трогаем - ставим None, если стоит None то поле только кликается,
    # что бы успеть отследить на каком поле находится тест
    # В отличие от create надо отдельно войти в форму и подтвердить изменения
    #     wd = self.app.wd
    #     if contact.first_name is not None:
    #         wd.find_element_by_xpath("//input[@name='firstname']").click()
    #         wd.find_element_by_xpath("//input[@name='firstname']").clear()
    #         wd.find_element_by_xpath("//input[@name='firstname']").send_keys(contact.first_name)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='firstname']").click()
    #
    #     if contact.mid_name is not None:
    #         wd.find_element_by_xpath("//input[@name='middlename']").click()
    #         wd.find_element_by_xpath("//input[@name='middlename']").clear()
    #         wd.find_element_by_xpath("//input[@name='middlename']").send_keys(contact.mid_name)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='middlename']").click()
    #
    #     if contact.last_name is not None:
    #         wd.find_element_by_xpath("//input[@name='lastname']").click()
    #         wd.find_element_by_xpath("//input[@name='lastname']").clear()
    #         wd.find_element_by_xpath("//input[@name='lastname']").send_keys(contact.last_name)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='lastname']").click()
    #
    #     if contact.nick_name is not None:
    #         wd.find_element_by_xpath("//input[@name='nickname']").click()
    #         wd.find_element_by_xpath("//input[@name='nickname']").clear()
    #         wd.find_element_by_xpath("//input[@name='nickname']").send_keys(contact.nick_name)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='nickname']").click()
    #
    #     if contact.company is not None:
    #         wd.find_element_by_xpath("//input[@name='company']").click()
    #         wd.find_element_by_xpath("//input[@name='company']").clear()
    #         wd.find_element_by_xpath("//input[@name='company']").send_keys(contact.company)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='company']").click()
    #
    #     if contact.title is not None:
    #         wd.find_element_by_xpath("//input[@name='title']").click()
    #         wd.find_element_by_xpath("//input[@name='title']").clear()
    #         wd.find_element_by_xpath("//input[@name='title']").send_keys(contact.title)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='title']").click()
    #
    #     if contact.address is not None:
    #         wd.find_element_by_xpath("//textarea[@name='address']").click()
    #         wd.find_element_by_xpath("//textarea[@name='address']").clear()
    #         wd.find_element_by_xpath("//textarea[@name='address']").send_keys(contact.address)
    #     else:
    #         wd.find_element_by_xpath("//textarea[@name='address']").click()
    #
    #     if contact.home_tel is not None:
    #         wd.find_element_by_xpath("//input[@name='home']").click()
    #         wd.find_element_by_xpath("//input[@name='home']").clear()
    #         wd.find_element_by_xpath("//input[@name='home']").send_keys(contact.home_tel)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='home']").click()
    #
    #     if contact.mob_tel is not None:
    #         wd.find_element_by_xpath("//input[@name='mobile']").click()
    #         wd.find_element_by_xpath("//input[@name='mobile']").clear()
    #         wd.find_element_by_xpath("//input[@name='mobile']").send_keys(contact.mob_tel)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='mobile']").click()
    #
    #     if contact.work_tel is not None:
    #         wd.find_element_by_xpath("//input[@name='work']").click()
    #         wd.find_element_by_xpath("//input[@name='work']").clear()
    #         wd.find_element_by_xpath("//input[@name='work']").send_keys(contact.work_tel)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='work']").click()
    #
    #     if contact.fax_tel is not None:
    #         wd.find_element_by_xpath("//input[@name='fax']").click()
    #         wd.find_element_by_xpath("//input[@name='fax']").clear()
    #         wd.find_element_by_xpath("//input[@name='fax']").send_keys(contact.fax_tel)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='fax']").click()
    #
    #     if contact.email is not None:
    #         wd.find_element_by_xpath("//input[@name='email']").click()
    #         wd.find_element_by_xpath("//input[@name='email']").clear()
    #         wd.find_element_by_xpath("//input[@name='email']").send_keys(contact.email)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='email']").click()
    #
    #     if contact.email2 is not None:
    #         wd.find_element_by_xpath("//input[@name='email2']").click()
    #         wd.find_element_by_xpath("//input[@name='email2']").clear()
    #         wd.find_element_by_xpath("//input[@name='email2']").send_keys(contact.email2)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='email2']").click()
    #
    #     if contact.email3 is not None:
    #         wd.find_element_by_xpath("//input[@name='email3']").click()
    #         wd.find_element_by_xpath("//input[@name='email3']").clear()
    #         wd.find_element_by_xpath("//input[@name='email3']").send_keys(contact.email3)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='email3']").click()
    #
    #     if contact.homepage_url is not None:
    #         wd.find_element_by_xpath("//input[@name='homepage']").click()
    #         wd.find_element_by_xpath("//input[@name='homepage']").clear()
    #         wd.find_element_by_xpath("//input[@name='homepage']").send_keys(contact.homepage_url)
    #     else:
    #         wd.find_element_by_xpath("//input[@name='homepage']").click()
    #
    #     if contact.bday is not None:
    #         bday_locator = f'select[name="bday"] > option[value="{contact.bday}"]'
    #         wd.find_element_by_xpath("//select[@name='bday']").click()
    #         wd.find_element_by_css_selector(bday_locator).click()
    #     else:
    #         wd.find_element_by_xpath("//select[@name='bday']").click()
    #
    #     if contact.bmonth is not None:
    #         bmonth_locator = f'select[name="bmonth"] > option[value="{contact.bmonth}"]'
    #         wd.find_element_by_xpath("//select[@name='bmonth']").click()
    #         wd.find_element_by_css_selector(bmonth_locator).click()
    #     else:
    #         wd.find_element_by_xpath("//select[@name='bmonth']").click()
    #
    #     if contact.byear is not None:
    #         wd.find_element_by_xpath("(//input[@name='byear'])[1]").click()
    #         wd.find_element_by_xpath("(//input[@name='byear'])[1]").clear()
    #         wd.find_element_by_xpath("(//input[@name='byear'])[1]").send_keys(contact.byear)
    #     else:
    #         wd.find_element_by_xpath("(//input[@name='byear'])[1]").click()
    #
    #     if contact.ayear is not None:
    #         aday_locator = f'select[name="aday"] > option[value="{contact.aday}"]'
    #         wd.find_element_by_xpath("//select[@name='aday']").click()
    #         wd.find_element_by_css_selector(aday_locator).click()
    #     else:
    #         wd.find_element_by_xpath("//select[@name='aday']").click()
    #
    #     if contact.ayear is not None:
    #         amonth_locator = f'select[name="amonth"] > option[value="{contact.amonth}"]'
    #         wd.find_element_by_xpath("//select[@name='amonth']").click()
    #         wd.find_element_by_css_selector(amonth_locator).click()
    #     else:
    #         wd.find_element_by_xpath("//select[@name='amonth']").click()
    #
    #     if contact.ayear is not None:
    #         wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
    #         wd.find_element_by_xpath("(//input[@name='ayear'])[1]").clear()
    #         wd.find_element_by_xpath("(//input[@name='ayear'])[1]").send_keys(contact.ayear)
    #     else:
    #         wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
