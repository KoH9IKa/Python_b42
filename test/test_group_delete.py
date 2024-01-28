import time
from model.group_info import Group


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.add_empty_group(amount=1)
    app.group.delete_first_group()



