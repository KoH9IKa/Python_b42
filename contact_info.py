class Contact:
    def __init__(self, first_name, mid_name, last_name, nick_name, photo, title, company, address,
                 home_tel, mob_tel, work_tel, fax_tel, email, email_2, email_3, homepage_url):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mob_tel = mob_tel
        self.work_tel = work_tel
        self.fax_tel = fax_tel
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage_url = homepage_url


class Date:
    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        self.byear = byear  # и a и b - вообще не трогаем изменение данных, может быть добавлю проверку на
        self.ayear = ayear  # 4х значный формат если надо будет
        # проверка вводимых данных, если не 1-31 то 0 (в селекторе будет выбран "-")
        bday = int(bday)
        if bday < 1 or bday > 31:
            bday = 0
        else:
            bday = bday
        self.bday = bday
        # то же самое для aday
        aday = int(aday)
        if aday < 1 or aday > 31:
            aday = 0
        else:
            aday = aday
        self.aday = aday
        # аналогично для месяца + выбор по номеру месяца из теста = значение которое будет выбрано в селекторе
        bmonth = int(bmonth)
        montlist = (
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December")
        if bmonth < 1 or bmonth > 12:
            bmonth = "-"
        else:
            i = bmonth - 1
            bmonth = montlist[i]
        self.bmonth = bmonth
        # то же самое для amonth
        amonth = int(amonth)
        if amonth < 1 or amonth > 12:
            amonth = "-"
        else:
            i = amonth - 1
            amonth = montlist[i]
        self.amonth = amonth
