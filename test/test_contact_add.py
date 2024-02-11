# -*- coding: utf-8 -*-
from model.contact_info import Contact
import pytest
import random
import string


def random_names(prefix, maxlen):
    symbols = string.ascii_letters * 5 + string.digits * 5 + "." * 5 + "-" * 5 + " " * 2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + "," * 3 + " " * 2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits + "@" * 5 + "." * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_url(maxlen):
    symbols = string.ascii_letters + string.digits + "." * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_month(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_year(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(first_name=first_name, mid_name=mid_name, last_name=last_name,
            address=address,
            mob_tel=mob_tel, work_tel=work_tel, home_tel=home_tel, fax_tel=fax_tel,
            email=email, email2=email2, email3=email3)

# testdata = [
    # Contact(first_name=first_name, mid_name=mid_name, last_name=last_name, nick_name=nick_name,
    #         title=title, company=company, address=address,
    #         mob_tel=mob_tel, work_tel=work_tel, home_tel=home_tel, fax_tel=fax_tel,
    #         email=email, email2=email2, email3=email3, homepage_url=homepage_url,
    #         bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear)
    for first_name in ["", random_names("first_name", 10)]
    for mid_name in ["", random_names("mid_name", 10)]
    for last_name in ["", random_names("last_name", 10)]
    # for nick_name in ["", random_names("nick_name", 5)]
    # for title in ["", random_names("title", 10)]
    # for company in ["", random_names("mid_name", 10)]
    for address in ["", random_address(30)]
    for mob_tel in [random_phone("+7", 15)]
    for work_tel in [random_phone("+7", 10)]
    for home_tel in [random_phone("+7", 10)]
    for fax_tel in [random_phone("+7", 10)]
    for email in [random_email(10)]
    for email2 in [random_email(20)]
    for email3 in [random_email(30)]
    # for homepage_url in ["", random_url(20, 3)]
    # for bday in [None, random_day(2)]
    # for bmonth in [None, random_month(2)]
    # for byear in ["", random_year(4)]
    # for aday in [None, random_day(2)]
    # for amonth in [None, random_month(2)]
    # for ayear in ["", random_year(4)]
]


# # отладочный набор
# testdata = [
#     Contact(first_name=first_name, mid_name=mid_name, last_name=last_name, nick_name=nick_name,
#             title=title, company=company, address=address,
#             mob_tel=mob_tel, work_tel=work_tel, home_tel=home_tel, fax_tel=fax_tel,
#             email=email, email2=email2, email3=email3, homepage_url=homepage_url,
#             bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear)
#     for first_name in [random_names("first_name", 10)]
#     for mid_name in [random_names("mid_name", 10)]
#     for last_name in [random_names("last_name", 10)]
#     for nick_name in [random_names("nick_name", 10)]
#     for title in [random_names("title", 10)]
#     for company in [random_names("mid_name", 10)]
#     for address in [random_address(5, 5, 5, 3)]
#     for mob_tel in [random_phone("+7", 10)]
#     for work_tel in [random_phone("+7", 10)]
#     for home_tel in [random_phone("+7", 10)]
#     for fax_tel in [random_phone("+7", 10)]
#     for email in [random_email(5, 5, 3)]
#     for email2 in [random_email(5, 5, 3)]
#     for email3 in [random_email(5, 5, 3)]
#     for homepage_url in [random_url(20, 3)]
#     for bday in [random_day(1)]
#     for bmonth in [random_month(1)]
#     for byear in [random_year(4)]
#     for aday in [random_day(1)]
#     for amonth in [random_month(1)]
#     for ayear in [random_year(4)]
# ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_bot_but(app, contact):
    # positive test with bottom enter button
    app.contact.open_contacts_page()
    old_contact = app.contact.get_all_contacts_list()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(contact)
    app.contact.press_bottom_enter_button()
    app.contact.open_contacts_page()
    new_contact = app.contact.get_all_contacts_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    # noinspection PyTypeChecker
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_add_contact_top_but(app, contact):
#     # positive test with top enter button + link for add next address + add one more default address
#     app.contact.open_contacts_page()
#     old_contact = app.contact.get_contact_list()
#     app.contact.add_new_contact()
#     app.contact.fill_form_with_check(contact)
#     app.contact.press_top_enter_button()
#     # check that next address link also is working and go to home page
#     app.contact.open_contacts_page()
#     assert len(old_contact) + 1 == app.contact.count()
#     new_contact = app.contact.get_contact_list()
#     old_contact.append(contact)
#     # noinspection PyTypeChecker
#     assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
#
#
# def test_add_some_contact(app):  # используем если надо сразу несколько групп сделать указывая amount
#     app.contact.add_new_contact()
#     amount = 20
#     if app.contact.count() < amount:
#         app.contact.add_default_filled_contact(amount)

# чистим перед стартом
# def test_delete_all_contacts(app):  # Тест удаления ВСЕХ записей через чекбокс внизу страницы
#     amount = 3
#     if app.contact.count() < amount:
#         app.contact.add_default_empty_contact(amount)  # делаем несколько и удаляем все
#     app.contact.open_contacts_page()
#     app.contact.select_all_checkbox()
#     app.contact.delete_button_in_table()
#     assert app.contact.count() == 0
