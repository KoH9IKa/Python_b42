class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='delete'])[1]").click()
        self.return_to_groups_page()

    def edit_first_group_in_table(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])[1]").click()

    def edit_or_create_with_check(self, group):
        # использовать вместе с param_check_with_name_loc
        locator_name = "group_name"
        locator_header = "group_header"
        locator_footer = "group_footer"
        self.param_check_with_name_loc(group.name, locator_name)
        self.param_check_with_name_loc(group.header, locator_header)
        self.param_check_with_name_loc(group.footer, locator_footer)

    def param_check_with_name_loc(self, param, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(param)
        else:
            wd.find_element_by_name(locator).click()
        return
