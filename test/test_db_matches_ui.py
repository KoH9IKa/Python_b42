from model.group_info import Group
from timeit import timeit


def test_group_list(app, db):
    ui_list = app.group.get_groups_list()
    app.group.open_groups_page()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_db_groups_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_timeit_group_list(app, db):
    print(timeit(lambda: app.group.get_groups_list(), number=1))
    app.group.open_groups_page()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    print(timeit(lambda: map(clean, db.get_db_groups_list()), number=1000))
    assert True  # (ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
