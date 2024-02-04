# -*- coding: utf-8 -*-
from model.group_info import Group
import time


def test_add_group_with_description(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.new_group_button()
    group = Group(name="aqwerty", header="new_group_header", footer="new_group_footer")
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    # noinspection PyTypeChecker
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_group_with_description1(app):
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     app.group.new_group_button()
#     group = Group(name="", header="", footer="")
#     app.group.fill_form_with_check(group)
#     app.group.submit()
#     app.group.open_groups_page()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     # noinspection PyTypeChecker
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

