import time

from model.group import Group


def test_update_first_group(app):
    app.group.open_groups_page()
    app.group.edit_first_group_in_table()
    app.group.edit_or_create_with_check(Group(name="old header",
                                              footer="old footer"))
    app.group.submit_update()
    app.group.open_groups_page()
