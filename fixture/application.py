from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='C:\\PycharmProjects\\brwsr_drvrs\\chrmdrvr 120.0.6099.109.exe')
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # self.wd = webdriver.Chrome(executable_path='C:\\PycharmProjects\\brwsr_drvrs\\chrmdrvr 120.0.6099.109.exe',
        #                            options=options)
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(0.5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            # noinspection PyStatementEffect
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("Logout")) > 0):
            wd.get("http://localhost/addressbook/")  # если мы не вошли или находимся не на хоум пейдж - идём по адресу
        else:
            pass  # если уже на домашней и вошли - пропускаем шаг

    def destroy(self):
        self.wd.quit()
