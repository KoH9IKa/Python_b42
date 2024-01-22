class Contact:
    def __init__(self, first_name, mid_name, last_name, nick_name,
                 photo, title, company, address,
                 home_tel, mob_tel, work_tel, fax_tel, email, email2, email3, homepage_url,
                 bday, aday, bmonth, amonth, byear, ayear):
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
        self.email2 = email2
        self.email3 = email3
        self.homepage_url = homepage_url
        self.ayear = ayear
        self.byear = byear
        self.aday = aday
        self.bday = bday
        # self.aday = self.day(aday)
        # self.bday = self.day(bday)
        self.amonth = self.month_calc(amonth)
        self.bmonth = self.month_calc(bmonth)

    def month_calc(self, month):
        # input check, if month == 1..12 then day = 1..12, else day = "-"
        try:
            if month is not None:  # так как в месяц может прилететь None и тест упадёт
                int_month = int(month)
                montlist = ("January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November", "December")
                i = int_month - 1
                int_month = montlist[i]
            else:
                int_month = None
        except:
            int_month = ""
        return int_month
