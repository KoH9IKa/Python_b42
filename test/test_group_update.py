import time
from model.group_info import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.add_group(amount=1)
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="SUPER NEW name")
    group.id = old_groups[0].id
    app.group.edit_first_group_in_table()
    app.group.fill_form_with_check(group)
    app.group.submit_update()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    # noinspection PyTypeChecker
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




