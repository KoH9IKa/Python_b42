from random import randrange
from model.contact_info import Contact


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
    ui_contacts = app.contact.get_all_contacts_list()
    db_contacts = db.get_db_contacts_list()
    assert db_contacts == sorted(ui_contacts, key=Contact.id_or_max)


