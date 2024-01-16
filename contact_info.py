class Contact:
    def __init__(self, first_name, mid_name, last_name, nick_name,
                 photo, title, company, address,
                 home_tel, mob_tel, work_tel, fax_tel, email, email_2, email_3, homepage_url,
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
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage_url = homepage_url
        self.ayear = ayear
        self.byear = byear
        self.aday = aday
        self.bday = bday
        # self.aday = self.day(aday)
        # self.bday = self.day(bday)
        self.amonth = self.month(amonth)
        self.bmonth = self.month(bmonth)

    # def day(self, day):
    #     # input check, if day == 1..31 then day = 1..31, else day = "-"
    #     int_day = int(day)
    #     if int_day < 1 or int_day > 31:
    #         int_day = 0
    #     else:
    #         int_day = day
    #     return int_day

    def month(self, month):
        # input check, if month == 1..12 then day = 1..12, else day = "-"
        int_month = int(month)
        montlist = ("January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December")
        i = int_month - 1
        int_month = montlist[i]
        return int_month
