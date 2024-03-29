# from model.contact_info import Contact
# from model.group_info import Group
# from fixture.orm import ORMFixture
# from datetime import datetime
#
# orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# group_name_raw = datetime.now()
# contact_first_name_raw = datetime.now()
# group_id = None
# contact1_id = []
# contact2_id = []
#
#
# def test_add_contact_to_created_group_crocodile(app, db):
#     global group_id
#     global contact1_id
#     global contact2_id
#     group_name = ("group " + str(group_name_raw)[:-7])  # �������� �� ����� ������
#     contact1_first_name = ("contact_1 " + str(contact_first_name_raw))[:-7]
#     # ������ ����������� ������, ������� ����� ����������� � �����
#     app.group.add_group_with_data(Group(name=group_name))
#     # ����� ����� � ������ ������ � ui � ����� � �� id
#     if group_id is None:
#         group_id = app.group.get_group_id_from_ui_by(name=group_name)
#     # ������ �������, ������� ����� ����������� � �����
#     app.contact.add_contact_with_data(Contact(first_name=contact1_first_name))
#     # ����� ����� � ���������� �������� id � ui
#     if len(contact1_id) == 0:
#         contact1_id = app.contact.get_contact_id_from_ui_by(first_name=contact1_first_name)
#     # � ����� ������� ���������� ��� ����, �������� ��������� �������� ������� � ���������� ��� � ������ �������� ������
#     # ��������� ��� ������ ������ ����������
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
#     # ��������� ������ ������� � ������
#     app.contact.add_contact_to_group(contact1_id, group_id)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     contacts_in_group_ui = app.contact.get_all_contacts_list()  # ���� ������ ��������� �� ui
#     contacts_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # � ������ �� ���� ��� ���������
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # ������� ����� ���������� 1 �������� � ������ �� 1
#     assert (sorted(contacts_in_group_ui, key=Contact.id_or_max)
#             == sorted(contacts_in_group_db, key=Contact.id_or_max))  # ���������� �������� ����� ui � db
#     # ��������� 2-� ������� � ��������� ��� � �� �� ������, ���� �� ���� - ����� ��� ����� ����������������
#     contact2_first_name = ("contact_2 " + str(contact_first_name_raw))[:-7]
#     app.contact.add_contact_with_data(Contact(first_name=contact2_first_name))
#     # ����� ����� � ���������� �������� id � ui
#     if len(contact2_id) == 0:
#         contact2_id = app.contact.get_contact_id_from_ui_by(first_name=contact2_first_name)
#     app.contact.add_contact_to_group(contact2_id, group_id)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     contacts2_in_group_ui = app.contact.get_all_contacts_list()  # ���� ������ ��������� �� ui
#     contacts2_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # � ������ �� ���� ��� ���������
#     assert len(contacts2_in_group_db) == 2  # ������� ����� ���������� 1 �������� � ������ �� 2
#     assert (sorted(contacts2_in_group_ui, key=Contact.id_or_max)
#             == sorted(contacts2_in_group_db, key=Contact.id_or_max))  # ���������� �������� ����� ui � db
#
#
# def test_delete_contact_from_group_crocodile(app, db):
#     global group_id
#     global contact1_id
#     global contact2_id
#     # 2� �������� ����� - ������� �� ������ �������� �� 1
#     app.contact.remove_contact_from_group(contact1_id, group_id)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     contacts3_in_group_ui = app.contact.get_all_contacts_list()  # ���� ������ ��������� �� ui
#     contacts3_in_group_db = orm.get_contacts_in_group(Group(id=group_id))  # � ������ �� ���� ��� ���������
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 1  # ����� �������� 1 �������� � ������ ������� 1
#     assert (sorted(contacts3_in_group_ui, key=Contact.id_or_max)
#             == sorted(contacts3_in_group_db, key=Contact.id_or_max))  # ���������� �������� ����� ui � db
#     app.contact.remove_contact_from_group(contact2_id, group_id)
#     app.contact.select_group_of_contacts_to_display(group_id)
#     # ��� ������ ����������� ������ ��� ��� ��� ������ �� ������ ���� � �����
#     assert len(orm.get_contacts_in_group(Group(id=group_id))) == 0
