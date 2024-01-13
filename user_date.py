class Name:
    def __init__(self, first_name, mid_name, last_name, nick_name):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nick_name = nick_name


class Other:
    def __init__(self, photo, title, company):
        self.photo = photo
        self.title = title
        self.company = company


class Address:
    def __init__(self, address):
        self.address = address


class Phone:
    def __init__(self, home_tel, mob_tel, work_tel, fax_tel):
        self.home_tel = home_tel
        self.mob_tel = mob_tel
        self.work_tel = work_tel
        self.fax_tel = fax_tel


class Email:
    def __init__(self, email, email_2, email_3, homepage_url):
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage_url = homepage_url


class Date:
    # only hardcode now :)
    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
