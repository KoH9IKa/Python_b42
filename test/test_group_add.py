# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_with_description(app):
    app.group.open_groups_page()
    app.group.new_group()
    app.group.edit_or_create_with_check(Group(name="new_group", header="new_group_header", footer="new_group_footer"))
    app.group.submit()
    app.group.return_to_groups_page()


def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.new_group()
    app.group.edit_or_create_with_check(Group(name="", header="", footer=""))
    app.group.submit()
    app.group.return_to_groups_page()


