# -*- coding: utf-8 -*-
from model.group_info import Group
import time


def test_add_group_with_description(app):
    app.group.open_groups_page()
    app.group.new_group_button()
    app.group.fill_form_with_check(Group(name="new_group", header="new_group_header", footer="new_group_footer"))
    app.group.submit()


def test_add_group_with_description1(app):
    app.group.open_groups_page()
    app.group.new_group_button()
    app.group.fill_form_with_check(Group(name="new_group", header="new_group_header", footer="new_group_footer"))
    app.group.submit()

