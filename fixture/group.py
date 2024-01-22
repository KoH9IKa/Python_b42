class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups' page
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

    def edit_with_check(self, group):
        # использовать вместе с param_check_with_name_loc,
        # можно использовать вместо create только нужны self.open_groups_page() и wd.find_element_by_name("new").click()
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

    # def edit(self, group):
    #     # В тесте на изменение данных там где данные не трогаем - ставим None,
    #     если стоит None то поле только кликается, что бы успеть отследить на каком поле находится тест.
    #     # В отличие от create надо отдельно войти в форму и подтвердить изменения
    #     wd = self.app.wd
    #     if group.name is not None:
    #         wd.find_element_by_name("group_name").click()
    #         wd.find_element_by_name("group_name").clear()
    #         wd.find_element_by_name("group_name").send_keys(group.name)
    #     else:
    #         wd.find_element_by_name("group_name").click()
    #
    #     if group.header is not None:
    #         wd.find_element_by_name("group_header").click()
    #         wd.find_element_by_name("group_header").clear()
    #         wd.find_element_by_name("group_header").send_keys(group.header)
    #     else:
    #         wd.find_element_by_name("group_header").click()
    #
    #     if group.footer is not None:
    #         wd.find_element_by_name("group_footer").click()
    #         wd.find_element_by_name("group_footer").clear()
    #         wd.find_element_by_name("group_footer").send_keys(group.footer)
    #     else:
    #         wd.find_element_by_name("group_footer").click()
    #     wd.find_element_by_name("update").click()
