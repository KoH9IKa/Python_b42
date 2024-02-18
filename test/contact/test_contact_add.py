from model.contact_info import Contact


def test_add_contact_bot_but_data(app, data_contacts):
    contact = data_contacts
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


def test_add_contact_bot_but_json(app, json_contacts):
    contact = json_contacts
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
