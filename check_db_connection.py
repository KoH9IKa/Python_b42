import pymysql.cursors
from fixture.orm import ORMFixture
from model.group_info import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# try:
#     list = db.get_groups_list()
#     for item in list:
#         print(item)
#     print(len(list))
# finally:
#     pass  # db.destroy()

# try:
#     list = db.get_contacts_list()
#     for item in list:
#         print(item)
#     print(len(list))
# finally:
#     pass  # db.destroy()
#
try:
    list = db.get_contacts_in_group(Group(id="814"))
    for item in list:
        print(item)
    print(len(list))
finally:
    pass  # db.destroy()
