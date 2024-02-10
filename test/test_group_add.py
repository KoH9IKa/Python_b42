# -*- coding: utf-8 -*-
from model.group_info import Group
import pytest
import time
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Group(name=name, header=header, footer=footer)
        for name in ["", random_string("name", 10)]
        for header in ["", random_string("header", 20)]
        for footer in ["", random_string("footer", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group_with_description(app, group):
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


