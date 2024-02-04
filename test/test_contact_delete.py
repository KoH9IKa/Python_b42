import time
from selenium.webdriver.common.by import By

from model.contact_info import Contact


def test_delete_first_contact(app):  # Тест удаления первой записи
    if app.contact.count() < 1:
        app.contact.add_default_filled_contact(amount=1)  # делаем одну и удаляем одну
    app.contact.open_contacts_page()
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    app.contact.open_contacts_page()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    app.contact.open_contacts_page()
    assert old_contact == new_contact


def test_delete_all_contacts(app):  # Тест удаления ВСЕХ записей через чекбокс внизу страницы
    amount = 3
    if app.contact.count() < amount:
        app.contact.add_default_empty_contact(amount)  # делаем несколько и удаляем все
    app.contact.open_contacts_page()
    app.contact.select_all_checkbox()
    app.contact.delete_button_in_table()
    assert app.contact.count() == 0
