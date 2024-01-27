# -*- coding: utf-8 -*-
from model.contact_info import Contact


def test_add_address_bot_but(app):
    # positive test with bottom enter button
    app.address.add_new_address()
    # Месяц вводить цифрами от "1" до "12", День от "1" до "31", форма может принимать None
    app.address.edit_or_create_with_check(Contact(first_name="Валерий",
                                                  mid_name="Непомню",
                                                  last_name="Меладзе",
                                                  nick_name="Я_КРАСИВЫЙ",
                                                  title="сингер",
                                                  photo="",
                                                  company='ООО "Я Продюсер ВИА ГРЫ"',
                                                  address="7777777, г.Меладзовское, ул.Певцова, д.3",
                                                  mob_tel="+7(123)456 78 98",
                                                  work_tel="+7(123)456 78 99",
                                                  home_tel="+7(123)456 78 10",
                                                  fax_tel="+7(123)456 78 11",
                                                  email="email4@mail.ru",
                                                  email2="email5@mail.ru",
                                                  email3="email6@mail.ru",
                                                  homepage_url="https:\\www.homepage2.com",
                                                  bday="1", bmonth="12", byear="2023",  # валидный дд мм
                                                  aday="31", amonth="1", ayear="2003")  # валидный дд мм
                                          )
    app.address.press_bottom_enter_button()
    app.return_to_home_page()


def test_add_address_top_but(app):
    # positive test with top enter button + link for add next address
    app.address.add_new_address()
    # Месяц вводить цифрами от "1" до "12", День от "1" до "31", форма может принимать None
    app.address.edit_or_create_with_check(Contact(first_name="Константин",
                                                  mid_name="Андреевич",
                                                  last_name="Верченко",
                                                  nick_name="Костян",
                                                  title="QA Eng.",
                                                  photo="",
                                                  company='ООО "Мартышка и очки"',
                                                  address="298300, г.Васюканск, ул.Из Костылей Строителей, д.404",
                                                  mob_tel="+7(123)456 78 90",
                                                  work_tel="+7(123)456 78 91",
                                                  home_tel="+7(123)456 78 92",
                                                  fax_tel="+7(123)456 78 93",
                                                  email="email1@mail.ru",
                                                  email2="email2@mail.ru",
                                                  email3="email3@mail.ru",
                                                  homepage_url="https:\\www.homepage.com",
                                                  bday="31", bmonth="1", byear="1995",
                                                  aday="1", amonth="12", ayear="2022")
                                          )
    app.address.press_top_enter_button()
    # check that next address link also is working and go to home page
    app.address.add_next_address()
    app.return_to_home_page()
