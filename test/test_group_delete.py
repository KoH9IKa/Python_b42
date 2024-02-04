import time
from model.group_info import Group


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.add_empty_group(amount=1)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


