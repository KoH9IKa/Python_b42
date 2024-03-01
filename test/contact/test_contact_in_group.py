import random
import time
from random import randrange

from model.contact_info import Contact
from model.group_info import Group
from fixture.orm import ORMFixture
from datetime import datetime

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
name_raw = datetime.now()


def test_add_contact_to_created_group(app, db):
    # сделали группу и узнали её индекс, айди, что группа содержит
    group_name = ("group " + str(name_raw)[:-7])
    app.group.add_group_with_data(Group(name=group_name))
    group_id = app.group.get_group_id_from_ui_by(name=group_name)
    contact_first_name = ("contact " + str(name_raw))[:-7]
    app.contact.add_contact_with_data(Contact(first_name=contact_first_name))
    contact_id = app.contact.get_contact_id_from_ui_by(first_name=contact_first_name)
    contact_index = app.contact.get_contact_index_by_firstname(contact_first_name)
    contact = app.contact.get_all_contacts_list()[contact_index]
    # с этого момента начинается сам тест, выделяем созданный тестовый контакт и отправляем его в нужную тестовую группу
    old_contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # смотрим контакты до добавления
    assert len(old_contacts_in_group_db) == 0  # проверяем что в db их 0 (так как группа новая)
    app.contact.add_contact_to_group(contact_id, group_id)    # добавляем контакт в группу
    app.contact.select_group_of_contacts_to_display(group_id)
    old_contacts_in_group_db.append(contact)    # к старому списку добавляем новый контакт
    new_contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # узнаём новый список групп
    # сравниваем что старый список + контакт == новый список
    assert (sorted(old_contacts_in_group_db, key=Contact.id_or_max)
            == sorted(new_contacts_in_group_db, key=Contact.id_or_max))


def test_remove_contact_from_group(app, db):
    # ищем группу через ui/db, вдруг у нас уже есть группа с контактами
    # group_id = app.contact.find_first_group_with_contacts(min_len=1) # ищем группы через ui (так дольше)
    db_groups = db.list_of_groups_with_contacts()  # ищем группы через db (так быстрее)
    if len(db_groups) == 0:
        group_id = None
    else:
        group_id = random.choice(db_groups)
    if group_id is None:  # Если None, то создаём группу и контакт и добавляем контакт в эту же группу
        group_name = ("group remove " + str(name_raw)[:-7])
        app.group.add_group_with_data(Group(name=group_name))
        group_id = app.group.get_group_id_from_ui_by(name=group_name)
        contact_first_name = ("contact remove " + str(name_raw))[:-7]
        app.contact.add_contact_with_data(Contact(first_name=contact_first_name))
        contact_id = app.contact.get_contact_id_from_ui_by(first_name=contact_first_name)
        app.contact.add_contact_to_group(contact_id, group_id)
        app.contact.open_contacts_page()
    # с этого момента начинается сам тест
    app.contact.select_group_of_contacts_to_display(group_id)
    # открываем группу, где есть контакты
    contacts_in_group_ui = app.contact.get_contacts_list_in_group()
    # сравниваем контакты в группе до удаления контакта
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))
    # удаляем из группы случайный контакт(даже если он 1)
    index = randrange(len(contacts_in_group_ui))
    contact = app.contact.get_contacts_list_in_group()[index]
    app.contact.select_checkbox_by_index(index)  # выбираем контакт по индексу
    app.contact.remove_contact_from_group_button()  # удаляем контакт из группы
    contacts_in_group_ui.remove(contact)  # удаляем контакт из списка старых контактов ui
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # заново спрашиваем список контактов в группе
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))
