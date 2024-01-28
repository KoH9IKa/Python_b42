import time

from model.contact_info import Contact


def test_delete_first_address(app):  # Тест удаления первой записи
    if app.address.count() == 0:
        app.address.add_default_filled_address(amount=1)  # делаем одну - удалится одна
    app.address.open_address_page()
    app.address.delete_first_address()


def test_delete_all_address(app):  # Тест удаления ВСЕХ записей через чекбокс внизу страницы
    if app.address.count() == 0:
        app.address.add_default_empty_address(amount=3)  # делаем несколько и удаляем все
    app.address.open_address_page()
    app.address.select_all_checkbox()
    app.address.delete_button_in_table()
