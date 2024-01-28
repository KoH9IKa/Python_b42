import time
from model.group_info import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.add_group(amount=1)
    app.group.open_groups_page()
    app.group.edit_first_group_in_table()
    app.group.fill_form_with_check(Group(name="SUPER NEW name", header="just header", footer="some new footer"))
    app.group.submit_update()
