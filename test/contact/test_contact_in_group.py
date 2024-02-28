import random
from random import randrange

from model.contact_info import Contact
from model.group_info import Group
from fixture.orm import ORMFixture
from datetime import datetime

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
name_raw = datetime.now()


def test_add_contact_to_created_group(app, db):
    group_name = ("group " + str(name_raw)[:-7])  # обрезаем до целых секунд
    app.group.add_group_with_data(Group(name=group_name))
    # узнаём id созданной группы
    group_id = app.group.get_group_id_from_ui_by(name=group_name)
    contact_first_name = ("contact " + str(name_raw))[:-7]
    app.contact.add_contact_with_data(Contact(first_name=contact_first_name))
    # узнаём id созданного контакта
    contact_id = app.contact.get_contact_id_from_ui_by(first_name=contact_first_name)
    # с этого момента начинается сам тест, выделяем созданный тестовый контакт и отправляем его в нужную тестовую группу
    # проверяем через базу сколько в группе изначально контактов, должно быть 0 так как группа новая
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
    # добавляем контакт в группу
    app.contact.add_contact_to_group(contact_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts_in_group_ui = app.contact.get_all_contacts_list()  # Берём список контактов из ui
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # И список из базы для сравнения
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db


def test_remove_contact_from_group(app, db):
    # ищем группу через ui/db, вдруг у нас уже есть группа с контактами
    # group_id = app.contact.find_first_group_with_contacts(min_len=1) # ищем группы через ui (так дольше)
    db_groups = db.list_of_groups_with_contacts()  # ищем группы через db (так быстрее)
    if len(db_groups) == 0:
        group_id = None
    else:
        group_id = random.choice(db_groups)
    print(group_id)
    if group_id is not None:
        pass  # если нам вернулся не None, то пропускаем
    else:  # а если None то создаём группу и контакт и добавляем контакт в эту же группу
        group_name = ("group remove " + str(name_raw)[:-7])
        app.group.add_group_with_data(Group(name=group_name))
        group_id = app.group.get_group_id_from_ui_by(name=group_name)
        contact_first_name = ("contact remove " + str(name_raw))[:-7]
        app.contact.add_contact_with_data(Contact(first_name=contact_first_name))
        contact_id = app.contact.get_contact_id_from_ui_by(first_name=contact_first_name)
        app.contact.add_contact_to_group(contact_id, group_id)
    # с этого момента начинается сам тест
    app.contact.select_group_of_contacts_to_display(group_id)
    # сравниваем контакты в группе до
    contacts_in_group_ui = app.contact.get_all_contacts_list()
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))
    # удаляем из группы случайный контакт(даже если он 1)
    index = randrange(len(contacts_in_group_ui))
    app.contact.select_checkbox_by_index(index)
    app.contact.remove_contact_from_group_button()
    # сравниваем контакты оставшиеся в группе после
    contacts_in_group_ui = app.contact.get_all_contacts_list()
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))
