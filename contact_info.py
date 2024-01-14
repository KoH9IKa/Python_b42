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
    # пересчёт дня и месяца на то что бы введёное в тесте = введёное в форму из-за разности цифр локатора и месяцев
    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        # так как локатор на пустое поле [2] а на 31й день [33] то
        # нам надо добавить 2 к, например, 15 что бы в дату ввелось не 13 а 15е число
        bday = int(bday)
        if (bday >= 1) and (bday <= 31):
            bday += 2
        else:
            bday = 2

        self.bday = bday
        # аналогично для месяца
        bmonth = int(bmonth)
        if (bmonth >= 1) and (bmonth <= 12):
            bmonth += 1
        else:
            bmonth = 1
        self.bmonth = bmonth
        # год у нас просто поле
        self.byear = byear
        # так как локатор на пустое поле [2] а на 31й день [33] то
        # нам надо добавить 2 к, например, 15 что бы в дату ввелось не 13 а 15е число
        aday = int(aday)
        if (aday >= 1) and (aday <= 31):
            aday += 2
        else:
            aday = 2
        self.aday = aday
        # аналогично для месяца
        amonth = int(amonth)
        if (amonth >= 1) and (amonth <= 12):
            amonth +=1
        else:
            amonth = 1
        self.amonth = amonth
        # год у нас просто поле
        self.ayear = ayear

