from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.address import AddressHelper


class Application:

    def __init__(self):
        # self.wd = webdriver.Chrome(
        #     executable_path='C:\\PycharmProjects\\browser_drivers\\chromedriver 120.0.6099.109.exe')
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.address = AddressHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def return_to_home_page(self):
        wd = self.wd
        # return to home page
        wd.find_element_by_xpath("//a[normalize-space()='home']").click()
