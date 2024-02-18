from model.group_info import Group


def test_add_group_with_description_from_data(app, data_groups):
    group = data_groups
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    # noinspection PyTypeChecker
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_with_description_from_json(app, json_groups):
    group = json_groups
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    # noinspection PyTypeChecker
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
