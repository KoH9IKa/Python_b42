import pymysql.cursors
from model.group_info import Group
from model.contact_info import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_db_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list "
                           "where deprecated is null")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_db_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            # можно использовать если нет софтделит и в поле депрекейтед будет всегда null
            # cursor.execute("select id, firstname, lastname from addressbook")
            # но на всякий случай пропишем что бы после фикса софтделита у нас не сломался тест при не null значении
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 "
                           "from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname,
                                    address=address,
                                    home_tel=home, mob_tel=mobile, work_tel=work,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def list_of_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id FROM `address_in_groups`")
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list