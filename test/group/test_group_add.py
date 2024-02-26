from model.group_info import Group


# Тест на создание групп используя сгенерированные данные из data/groups.py и сравнением данных через ui
def test_add_group_with_description_from_data_check_ui(app, data_groups):
    group = data_groups
    app.group.open_groups_page()
    old_groups = app.group.get_groups_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Тест на создание групп используя сгенерированные данные из data/groups.json и сравнением данных через ui
def test_add_group_with_description_from_json_check_ui(app, json_groups):
    group = json_groups
    app.group.open_groups_page()
    old_groups = app.group.get_groups_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Тест на создание групп используя сгенерированные данные из data/groups.json и сравнением данных через db
def test_add_group_with_description_from_data_check_db(app, db, data_groups, check_ui):
    group = data_groups
    app.group.open_groups_page()
    old_groups = db.get_db_groups_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    new_groups = db.get_db_groups_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


# Тест на создание групп используя сгенерированные данные из data/groups.json и сравнением данных через db
def test_add_group_with_description_from_json_check_db(app, db, json_groups, check_ui):
    group = json_groups
    app.group.open_groups_page()
    old_groups = db.get_db_groups_list()
    app.group.new_group_button()
    app.group.fill_form_with_check(group)
    app.group.submit()
    app.group.open_groups_page()
    new_groups = db.get_db_groups_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)