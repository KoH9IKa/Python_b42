import random
import time
from selenium.webdriver.common.by import By
from random import randrange
from model.contact_info import Contact


# тест удаления первого контакта в списке в ui
def test_delete_first_contact(app):
    if app.contact.count() < 1:
        app.contact.add_default_filled_contact(amount=3)  # делаем одну и удаляем одну
    app.contact.open_contacts_page()
    old_contact = app.contact.get_all_contacts_list()
    app.contact.delete_first_contact()
    print("Удалён первый контакт")
    app.contact.open_contacts_page()
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_all_contacts_list()
    old_contact[0:1] = []
    app.contact.open_contacts_page()
    assert old_contact == new_contact


# Тест удаления случайной записи в таблице контактов
def test_delete_contact_by_index(app):
    if app.contact.count() < 3:
        app.contact.add_default_filled_contact(amount=5)  # делаем одну и удаляем одну
    app.contact.open_contacts_page()
    old_contact = app.contact.get_all_contacts_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    print("Удалён контакт с номером "+str(index+1))
    app.contact.open_contacts_page()
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_all_contacts_list()
    old_contact[index:index+1] = []
    app.contact.open_contacts_page()
    assert old_contact == new_contact


# Тест удаления ВСЕХ записей через чекбокс внизу страницы
def test_delete_all_contacts(app):
    amount = 3
    if app.contact.count() < amount:
        app.contact.add_default_empty_contact(amount)  # делаем несколько и удаляем все
    app.contact.open_contacts_page()
    app.contact.select_all_checkbox()
    app.contact.delete_button_in_table()
    assert app.contact.count() == 0


# Тест удаление записи по id записи из db с удалением через ui и сравнением данных db с db
def test_delete_contact_by_id_comparison_db_w_db(app, db, check_ui):
    if app.contact.count() < 3:
        app.contact.add_default_filled_contact(amount=5)  # делаем несколько и удаляем одну
    app.contact.open_contacts_page()
    old_contacts = db.get_db_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    old_contacts.remove(contact)
    new_contacts = db.get_db_contacts_list()
    assert old_contacts == new_contacts
    app.contact.open_contacts_page()
    if check_ui:
        assert new_contacts == sorted(app.contact.get_all_contacts_list(), key=Contact.id_or_max)

