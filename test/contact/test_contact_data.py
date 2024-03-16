from random import randrange
from model.contact_info import Contact
from fixture.orm import ORMFixture
# orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# Проверка данных контакта отображаемых на addressbook/ и edit.php
def test_check_contact_data_by_random_index(app):
    app.contact.open_contacts_page()
    contacts = app.contact.get_all_contacts_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_all_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert (contact_from_home_page.all_phones_from_home_page ==
            app.contact.merge_phones_like_on_home_page(contact_from_edit_page))
    assert (contact_from_home_page.all_emails_from_home_page ==
            app.contact.merge_emails_like_on_home_page(contact_from_edit_page))
    print(contact_from_home_page)  # вывод что бы смотреть что действительно то что сравнивали
    print(contact_from_edit_page)  # и то с чем сравнивали - имеют одинаковые данные по которым идёт проверка


def test_phones_on_view_page(app):
    app.contact.open_contacts_page()
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    app.contact.open_contacts_page()
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_view_page.mob_tel == contact_from_edit_page.mob_tel
    assert contact_from_view_page.work_tel == contact_from_edit_page.work_tel
    assert contact_from_view_page.fax_tel == contact_from_edit_page.fax_tel


def test_check_data_from_contacts_page_with_data_in_db(app, db):
    app.contact.open_contacts_page()
    contacts_db = sorted(db.get_db_contacts_list(), key=Contact.id_or_max)  # достаём и сортируем данные из таблицы
    contacts_homepage = sorted(app.contact.get_all_contacts_list(), key=Contact.id_or_max)  # тоже самое для данных с ui
    assert contacts_db == contacts_homepage  # сравниваем то что прописано в __eq__
    db_phones, db_emails = [], []  # создаём пустые списки для телефонов и почт из базы
    for db_contact in db.get_db_contacts_list(): # для всех контактов в базе перебираем
        db_phones.append(app.contact.merge_phones_like_on_home_page(db_contact))  # тут собираем через моржа телефоны
        db_emails.append(app.contact.merge_emails_like_on_home_page(db_contact))  # а тут собираем почты
    for index in range(0, (len(contacts_homepage))):  # теперь у нас есть 3 одинаковых списка с одинаковым range (наверное)
        assert contacts_homepage[index].all_emails_from_home_page == db_emails[index]  # в каждом контакте проверяем его олл имейлз с такой же строкой из базы
        assert contacts_homepage[index].all_phones_from_home_page == db_phones[index]  # тоже самое для телефонов
