# -*- coding: utf-8 -*-
from model.contact_info import Contact


def test_add_contact_bot_but(app):
    # positive test with bottom enter button
    app.contact.open_contacts_page()
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    # Месяц вводить цифрами от "1" до "12", День от "1" до "31", форма может принимать None
    contact = Contact(first_name="Валерий", mid_name="Непомню", last_name="Меладзе", nick_name="Я_КРАСИВЫЙ",
                      title="сингер", photo="", company='ООО "Я Продюсер ВИА ГРЫ"',
                      address="7777777, г.Меладзовское, ул.Певцова, д.3",
                      mob_tel="+7(123)456 78 98", work_tel="+7(123)456 78 99", home_tel="+7(123)456 78 10",
                      fax_tel="+7(123)456 78 11",
                      email="email4@mail.ru", email2="email5@mail.ru", email3="email6@mail.ru",
                      homepage_url="https:\\www.homepage2.com",
                      bday="1", bmonth="12", byear="2023",  # валидный дд мм
                      aday="31", amonth="1", ayear="2003")  # валидный дд мм
    app.contact.fill_form_with_check(contact)
    app.contact.press_bottom_enter_button()
    app.contact.open_contacts_page()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    # noinspection PyTypeChecker
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_add_contact_top_but(app):
    # positive test with top enter button + link for add next address + add one more default address
    app.contact.open_contacts_page()
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    # Месяц вводить цифрами от "1" до "12", День от "1" до "31", форма может принимать None
    contact = Contact(first_name="Константин", mid_name="Андреевич", last_name="Верченко", nick_name="Костян",
                      title="QA Eng.", photo="", company='ООО "Мартышка и очки"',
                      address="298300, г.Васюканск, ул.Из Костылей Строителей, д.404",
                      mob_tel="+7(123)456 78 90", work_tel="+7(123)456 78 91", home_tel="+7(123)456 78 92",
                      fax_tel="+7(123)456 78 93",
                      email="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
                      homepage_url="https:\\www.homepage.com",
                      bday="31", bmonth="1", byear="1995",
                      aday="1", amonth="12", ayear="2022")
    app.contact.fill_form_with_check(contact)
    app.contact.press_top_enter_button()
    # check that next address link also is working and go to home page
    app.contact.open_contacts_page()
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    # noinspection PyTypeChecker
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_add_some_contact(app):  #  используем если надо сразу штук (много) групп сделать
    app.contact.add_new_contact()
    amount = 20
    if app.contact.count() < amount:
        app.contact.add_default_filled_contact(amount)
