from model.contact_info import Contact


def test_add_address_bot_but(app):
    # positive test bottom delete button
    app.address.delete_first_address()
    app.return_to_home_page()
