import time
from model.group_info import Group
import random
from random import randrange


# сравнение данных обновления первой группы до изменения и после используя для сравнения только ui
def test_update_first_group_ui_with_ui_comparison(app):
    if app.group.count() == 0:
        app.group.add_group(amount=1)
    app.group.open_groups_page()
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = Group(name="adasgasdf6фывe")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index)
    app.group.fill_form_with_check(group)
    app.group.submit_update()
    app.group.open_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# сравнение данных обновления первой группы до изменения и после используя для сравнения только db
def test_update_first_group_db_with_db_comparison(app, db):
    old_groups_db = db.get_db_groups_list()
    if len(old_groups_db) == 0:
        app.group.add_group(amount=1)
    app.group.open_groups_page()
    group = old_groups_db[0]
    group_data = Group(name="adasgasdf6фывe")
    app.group.edit_group_by_id(group.id)
    app.group.fill_form_with_check(group_data)
    app.group.submit_update()
    app.group.open_groups_page()
    new_groups_db = db.get_db_groups_list()
    old_groups_db[0] = group
    assert sorted(old_groups_db, key=Group.id_or_max) == sorted(new_groups_db, key=Group.id_or_max)





