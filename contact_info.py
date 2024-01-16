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
        self.year(ayear, byear)
        self.day(aday, bday)
        self.month(amonth, bmonth)

    def day(self, aday, bday):
        # input check, if day == 1..31 then day = 1..31, else day = "-"
        bday = int(bday)
        if bday < 1 or bday > 31:
            bday = 0
        else:
            bday = bday
        self.bday = bday

        aday = int(aday)
        if aday < 1 or aday > 31:
            aday = 0
        else:
            aday = aday
        self.aday = aday

    def month(self, amonth, bmonth):
        # input check, if month == 1..12 then day = 1..12, else day = "-"
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

        amonth = int(amonth)
        if amonth < 1 or amonth > 12:
            amonth = "-"
        else:
            i = amonth - 1
            amonth = montlist[i]
        self.amonth = amonth

    def year(self, ayear, byear):
        # no check but if it will in future?
        self.byear = byear
        self.ayear = ayear