from model.contact_info import Contact
import time

import random
from random import randrange


# Удаление случайного контакта взятого по случайному index со страницы и сравнение данных ui с ui
def test_update_contact_by_random_index_in_ui(app):
    app.contact.open_contacts_page()
    if app.contact.count() == 0:
        app.contact.add_default_filled_contact(amount=3)
    old_contact = app.contact.get_all_contacts_list()
    index = randrange(len(old_contact))
    app.contact.edit_contact_by_index(index)
    contact = Contact(first_name="73734ацуа", last_name="34цуацауацу5")
    app.contact.fill_form_with_check(contact)
    app.contact.press_top_update_button()
    app.open_home_page()
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_all_contacts_list()
    contact.id = old_contact[index].id
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# Удаление случайного контакта взятого по случайному id из таблицы и сравнение данных db с db
def test_update_contact_by_random_id_in_db(app, db, check_ui):
    app.contact.open_contacts_page()
    if app.contact.count() == 0:
        app.contact.add_default_filled_contact(amount=3)
    old_contacts = db.get_db_contacts_list()
    contact = random.choice(old_contacts)
    contact_index = old_contacts.index(contact)
    app.contact.edit_contact_by_id(contact.id)
    contact = Contact(first_name="что-то-новое", last_name="и-тут-тоже")
    app.contact.fill_form_with_check(contact)
    app.contact.press_top_update_button()
    app.open_home_page()
    new_contacts = db.get_db_contacts_list()
    old_contacts[contact_index] = contact
    assert old_contacts == sorted(new_contacts, key=Contact.id_or_max)
