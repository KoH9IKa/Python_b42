from pytest_bdd import given, when, then, parsers
from model.group_info import Group


@given('group list')
def groups_list(db):
    db.get_db_groups_list()


@given('group with {name} {header} {footer}')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('add new group')
def add_new_group(app, new_group):
    app.group.add_group(new_group)


@then('new groups list is equal to old groups list with added group')
def verify_group_added(db, groups_list, new_group):
    old_groups = groups_list
    new_groups = db.get_db_groups_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)