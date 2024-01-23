import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        wd.find_element_by_xpath("//input[@name='user']").click()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").click()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        time.sleep(1)  # этот нужен, что бы предыдущая страница успела прогрузиться
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)  # а этот что бы разлогин успел произойти перед следующим тестом

