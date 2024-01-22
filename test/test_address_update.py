from model.contact_info import Contact
import time


def test_update_last_by_lastname_address(app):
    app.session.login(username="admin", password="secret")
    app.address.sort_by_last_name()
    time.sleep(0.1)
    app.address.sort_by_last_name()
    time.sleep(0.1)
    app.address.edit_first_address_in_table()
    time.sleep(0.1)
    # там где меняем - новое значение, там где не трогаем - None
    app.address.edit_or_create_with_check(Contact(first_name="Андрй",
                                                  mid_name=None,
                                                  last_name="Андреев",
                                                  nick_name="qwerty",
                                                  title=None,
                                                  photo=None,
                                                  company=None,
                                                  address=None,
                                                  mob_tel=None,
                                                  work_tel=None,
                                                  home_tel=None,
                                                  fax_tel=None,
                                                  email="andreyka@gmail.com",
                                                  email2=None,
                                                  email3=None,
                                                  homepage_url=None,
                                                  bday=None, bmonth=None, byear=None,
                                                  aday=None, amonth=None, ayear=None))
    time.sleep(0.1)
    app.address.press_top_update_button()
    app.return_to_home_page()
    app.session.logout()
