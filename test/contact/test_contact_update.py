from model.contact_info import Contact
import time
from random import randrange


def test_update_random_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:  # если нечего изменять - делаем несколько (что бы было что изменять)
        app.contact.add_default_filled_contact(amount=3)
    old_contact = app.contact.get_all_contacts_list()
    index = randrange(len(old_contact))
    app.contact.edit_contact_by_index(index)
    # там где меняем - новое значение, там где не трогаем - None либо не пишем ничего
    contact = Contact(first_name="73734ацуа", last_name="34цуацауацу5")
    app.contact.fill_form_with_check(contact)
    app.contact.press_top_update_button()
    app.open_home_page()
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_all_contacts_list()
    contact.id = old_contact[index].id
    old_contact[index] = contact
    # noinspection PyTypeChecker
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
