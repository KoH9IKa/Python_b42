
class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_next_address(self):
        wd = self.app.wd
        # return to form for add next address
        wd.find_element_by_xpath("//a[normalize-space()='add next']").click()

    def press_top_enter_button(self):
        wd = self.app.wd
        # top "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[1]").click()

    def press_bottom_enter_button(self):
        wd = self.app.wd
        # bottom "enter" button usage
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_xpath("//select[@name='amonth']").click()
        wd.find_element_by_css_selector(amonth_locator).click()
        # Anniversary year setting
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").click()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").clear()
        wd.find_element_by_xpath("(//input[@name='ayear'])[1]").send_keys(contact.ayear)
        # так как кнопок подтверждения на форме 2 - их сюда пока не помещал
