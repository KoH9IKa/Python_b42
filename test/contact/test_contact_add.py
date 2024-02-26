from model.contact_info import Contact


# добавлени€ контакта с данными из data/contacts.py использу€ верхнюю кнопку сохранени€ и проверка результата через ui
def test_add_contact_bot_but_data_ui_w_ui_comparison(app, data_contacts):
    contact = data_contacts
    app.contact.open_contacts_page()
    old_contact = app.contact.get_all_contacts_list()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(contact)
    app.contact.press_bottom_enter_button()
    app.contact.open_contacts_page()
    new_contact = app.contact.get_all_contacts_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# добавлени€ контакта с данными из data/contacts.json использу€ верхнюю кнопку сохранени€ и проверка результата через ui
def test_add_contact_bot_but_json_ui_w_ui_comparison(app, json_contacts):
    contact = json_contacts
    app.contact.open_contacts_page()
    old_contact = app.contact.get_all_contacts_list()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(contact)
    app.contact.press_bottom_enter_button()
    app.contact.open_contacts_page()
    new_contact = app.contact.get_all_contacts_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# добавлени€ контакта с данными из data/contacts.json использу€ верхнюю кнопку сохранени€ и проверка результата через db
def test_add_contact_bot_but_json_db_w_db_comparison(app, db, json_contacts, check_ui):
    contact = json_contacts
    app.contact.open_contacts_page()
    old_contacts = db.get_db_contacts_list()
    app.contact.add_new_contact()
    app.contact.fill_form_with_check(contact)
    app.contact.press_bottom_enter_button()
    app.contact.open_contacts_page()
    new_contacts = db.get_db_contacts_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert old_contacts == sorted(app.contact.get_all_contacts_list(), key=Contact.id_or_max)
