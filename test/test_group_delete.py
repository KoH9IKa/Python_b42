import time
from model.group_info import Group
from random import randrange


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.add_empty_group(amount=1)
    old_groups = app.group.get_group_list()
    index = 0  # real position of group is +1
    app.group.delete_group_by_index(index)
    app.group.open_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_some_group(app):
    app.group.open_groups_page()
    if app.group.count() < 5:
        app.group.add_empty_group(amount=10)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.group.open_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

