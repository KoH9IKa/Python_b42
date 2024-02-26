#  ORM = Object Relational Mapping
import dbm

from pony.orm import *
from datetime import datetime
from model.group_info import Group
from model.contact_info import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        deprecated = Optional(str, column='deprecated')
        contacts = Set(lambda: ORMFixture.ORMContact,
                       table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        mobile = Optional(str, column='mobile')
        home = Optional(str, column='home')
        work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, footer=group.footer, header=group.header)
        return list(map(convert, groups))

    @db_session
    def get_contacts_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.firstname, last_name=contact.lastname,
                           address=contact.address,
                           mob_tel=contact.mobile, home_tel=contact.home, work_tel=contact.work,
                           email=contact.email, email2=contact.email2, email3=contact.email3)

        return list(map(convert, contacts))

    @db_session
    def get_contacts_in_group(self, group):
        ormgroup = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(ormgroup.contacts)

    # @db_session
    # def get_contacts_in_group(self, group):
    #     ormgroup = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
    #     return self.convert_contacts_to_model(ormgroup.contacts)