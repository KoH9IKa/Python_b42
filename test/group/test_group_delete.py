import random
import time
from model.group_info import Group
from random import randrange

# Удаление первой группы в списке и проверка результата удаления только через ui
def test_delete_first_group_in_ui(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.add_empty_group(amount=1)
    old_groups = app.group.get_groups_list()
    index = 0  # real position of group is +1
    app.group.delete_group_by_index(index)
    app.group.open_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


# Удаление случайной группы в списке и проверка результата удаления только через ui
def test_delete_random_group_in_ui(app):
    app.group.open_groups_page()
    if app.group.count() < 5:
        app.group.add_empty_group(amount=10)
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.group.open_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


# Удаление случайной группы в таблице базы группы и проверка результата удаления только через db
def test_delete_random_group_in_db(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_db_groups_list()) < 5:
        app.group.add_empty_group(amount=10)
    old_groups = db.get_db_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    app.group.open_groups_page()
    new_groups = db.get_db_groups_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
