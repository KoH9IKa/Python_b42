from model.contact_info import Contact
import time


def test_update_last_by_lastname_address(app):
    app.open_home_page()
    if app.address.count() == 0:
        app.address.add_default_filled_address(amount=5)
    app.address.sort_by_last_name()  # Дважды жмём сортировку по last_name,
    app.address.sort_by_last_name()  # что бы первым в списке оказался последний по алфавиту
    app.address.edit_first_address_in_table()
    # там где меняем - новое значение, там где не трогаем - None либо не пишем ничего
    app.address.fill_form_with_check(Contact(first_name="Андрей",
                                             last_name="Андреев",
                                             nick_name="qwerty",
                                             email="andreyka@gmail.com"))
    app.address.press_top_update_button()
    app.open_home_page()



