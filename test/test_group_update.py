import time

from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group_in_table()
    app.group.edit_with_check(Group(name="old header",
                                    header=None,
                                    footer="old footer"))
    time.sleep(1)
    # app.group.open_groups_page()
    app.session.logout()
