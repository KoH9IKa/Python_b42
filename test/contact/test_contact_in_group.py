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


def test_add_contact_to_created_group_and_delete_contact_from_group(app, db):
    global group_id
    global contact1_id
    global contact2_id
    group_name = ("group " + str(group_name_raw)[:-7])  # обрезаем до целых секунд
    contact1_first_name = ("contact_1 " + str(contact_first_name_raw))[:-7]
    # создаЄм специальную группу, котора€ будет участвовать в тесте
    app.group.open_groups_page()
    app.group.new_group_button()
    app.group.fill_form_with_check(Group(name=group_name))
    app.group.submit()
    app.group.open_groups_page()
    # узнаЄм какой у группы индекс в ui и какой у неЄ id
    if group_id is None:
        group_id = app.group.get_group_id_by_name(group_name)
    # создаЄм контакт, который будет участвовать в тесте
    app.contact.open_contacts_page()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(Contact(first_name=contact1_first_name))
    app.contact.press_top_enter_button()
    app.contact.open_contacts_page()
    # узнаЄм какой у созданного контакта id в ui
    if len(contact1_id) == 0:
        contact1_id = app.contact.get_contact_id_by_firstname(contact1_first_name)
    # с этого момента начинаетс€ сам тест, выдел€ем созданный тестовый контакт и отправл€ем его в нужную тестовую группу
    # провер€ем что группа пуста€ изначально
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
    # добавл€ем первый контакт в группу
    app.contact.add_contact_to_group(contact1_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts_in_group_ui = app.contact.get_all_contacts_list()  # ЅерЄм список контактов из ui
    contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # » список из базы дл€ сравнени€
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # смотрим после добавлени€ 1 контакта в группе он 1
    assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db
    # добавл€ем 2-й контакт и добавл€ем его в ту же группу, если не надо - можно всю часть закомментировать
    contact2_first_name = ("contact_2 " + str(contact_first_name_raw))[:-7]
    app.contact.open_contacts_page()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(Contact(first_name=contact2_first_name))
    app.contact.press_top_enter_button()
    app.contact.open_contacts_page()
    # узнаЄм какой у созданного контакта id в ui
    if len(contact2_id) == 0:
        contact2_id = app.contact.get_contact_id_by_firstname(contact2_first_name)
    app.contact.add_contact_to_group(contact2_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts2_in_group_ui = app.contact.get_all_contacts_list()  # ЅерЄм список контактов из ui
    contacts2_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # » список из базы дл€ сравнени€
    assert len(contacts2_in_group_db) == 2  # смотрим после добавлени€ 1 контакта в группе их 2
    assert (sorted(contacts2_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts2_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db
    # 2€ половина теста - удал€ем из группы контакты по 1
    app.contact.remove_contact_from_group(contact1_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    contacts3_in_group_ui = app.contact.get_all_contacts_list()  # ЅерЄм список контактов из ui
    contacts3_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # » список из базы дл€ сравнени€
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # после удалени€ 1 контакта в группе осталс€ 1
    assert (sorted(contacts3_in_group_ui, key=Contact.id_or_max)
            == sorted(contacts3_in_group_db, key=Contact.id_or_max))  # сравниваем контакты через ui и db
    app.contact.remove_contact_from_group(contact2_id, group_id)
    app.contact.select_group_of_contacts_to_display(group_id)
    # нет смысла запрашивать списки так как тут ничего не должно быть в итоге
    assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0


#     # еще 1 вариант блока с удалением но использу€ кеш когда-то вз€тый,
#     # через ремув из кеша строки с контактов которую удалили из группы
#     # но требует некоторой переработки в самом тесте, оставил дл€ себ€
#
#     # 2€ половина теста - удал€ем из группы контакты по 1
#     contact = random.choice(contacts2_in_group_ui)
#     app.contact.remove_contact_from_group(contact.id, group_id)
#     contacts2_in_group_ui.remove(contact)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     contacts3_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # » список из базы дл€ сравнени€
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # после удалени€ 1 контакта в группе осталс€ 1
#     assert (sorted(contacts2_in_group_ui, key=Contact.id_or_max)
#             == sorted(contacts3_in_group_db, key=Contact.id_or_max))
#     contact = contacts2_in_group_ui[0]
#     app.contact.remove_contact_from_group(contact.id, group_id)
#     contacts2_in_group_ui.remove(contact)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
