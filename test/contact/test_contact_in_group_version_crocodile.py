from model.contact_info import Contact
from model.group_info import Group
from fixture.orm import ORMFixture
from datetime import datetime

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
group_name_raw = datetime.now()
contact_first_name_raw = datetime.now()
group_id = None
contact1_id = []
contact2_id = []


def test_add_contact_to_created_group_crocodile(app, db):
    global group_id
    global contact1_id
    global contact2_id
    group_name = ("group " + str(group_name_raw)[:-7])  # обрезаем до целых секунд
    contact1_first_name = ("contact_1 " + str(contact_first_name_raw))[:-7]
    # создаём специальную группу, которая будет участвовать в тесте
    app.group.add_group_with_data(Group(name=group_name))
    # узнаём какой у группы индекс в ui и какой у неё id
    if group_id is None:
        group_id = app.group.get_group_id_from_ui_by(name=group_name)
    # создаём контакт, который будет участвовать в тесте
    app.contact.add_contact_with_data(Contact(first_name=contact1_first_name))
    # узнаём какой у созданного контакта id в ui
    if len(contact1_id) == 0:
        contact1_id = app.contact.get_contact_id_from_ui_by(first_name=contact1_first_name)
    # с этого момента начинается сам тест, выделяем созданный тестовый контакт и отправляем его в нужную тестовую группу
    # проверяем что группа пустая изначально
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
    # добавляем первый контакт в группу
    app.contact.add_contact_to_group(contact1_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts_in_group_ui = app.contact.get_all_contacts_list()  # Берём список контактов из ui
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # И список из базы для сравнения
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # смотрим после добавления 1 контакта в группе он 1
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db
    # добавляем 2-й контакт и добавляем его в ту же группу, если не надо - можно всю часть закомментировать
    contact2_first_name = ("contact_2 " + str(contact_first_name_raw))[:-7]
    app.contact.add_contact_with_data(Contact(first_name=contact2_first_name))
    # узнаём какой у созданного контакта id в ui
    if len(contact2_id) == 0:
        contact2_id = app.contact.get_contact_id_from_ui_by(first_name=contact2_first_name)
    app.contact.add_contact_to_group(contact2_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts2_in_group_ui = app.contact.get_all_contacts_list()  # Берём список контактов из ui
    contacts2_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # И список из базы для сравнения
    assert len(contacts2_in_group_db) == 2  # смотрим после добавления 1 контакта в группе их 2
    assert (sorted(contacts2_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts2_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db


def test_delete_contact_from_group_crocodile(app, db):
    global group_id
    global contact1_id
    global contact2_id
    # 2я половина теста - удаляем из группы контакты по 1
    app.contact.remove_contact_from_group(contact1_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts3_in_group_ui = app.contact.get_all_contacts_list()  # Берём список контактов из ui
    contacts3_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # И список из базы для сравнения
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # после удаления 1 контакта в группе остался 1
    assert (sorted(contacts3_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts3_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db
    app.contact.remove_contact_from_group(contact2_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    # нет смысла запрашивать списки так как тут ничего не должно быть в итоге
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
