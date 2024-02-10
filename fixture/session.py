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
        time.sleep(0.2)  # этот нужен, что бы предыдущая страница успела прогрузиться
        wd.find_element_by_link_text("Logout").click()
        time.sleep(0.2)  # а этот что бы разлогин успел произойти перед следующим тестом

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
