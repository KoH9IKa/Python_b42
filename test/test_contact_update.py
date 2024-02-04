from model.contact_info import Contact
import time


def test_update_last_by_lastname_address(app):
    app.open_home_page()
    if app.contact.count() == 0:  # если нечего изменять - делаем несколько (что бы было что изменять)
        app.contact.add_default_filled_contact(amount=3)
    old_contact = app.contact.get_contact_list()
    app.contact.sort_by_last_name()  # Дважды жмём сортировку по last_name,
    app.contact.sort_by_last_name()  # что бы первым в списке оказался последний по алфавиту
    app.contact.edit_first_contact_in_table()
    # там где меняем - новое значение, там где не трогаем - None либо не пишем ничего
    contact = Contact(first_name="фывфывфывфыв", last_name="фывфывйцуйцвфыв")
    app.contact.fill_form_with_check(contact)
    app.contact.press_top_update_button()
    app.open_home_page()
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    contact.id = old_contact[0].id
    old_contact[0] = contact
    # noinspection PyTypeChecker
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
