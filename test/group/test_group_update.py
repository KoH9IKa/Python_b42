import time
from model.group_info import Group
from random import randrange


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.add_group(amount=1)
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="adasgasdf6фывe")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index)
    app.group.fill_form_with_check(group)
    app.group.submit_update()
    app.group.open_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    # noinspection PyTypeChecker
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




