# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_with_description(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", header="new_group_header", footer="new_group_footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


