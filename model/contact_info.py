from sys import maxsize


class Contact:
    def __init__(self, first_name=None, mid_name=None, last_name=None, nick_name=None,
                 photo=None, title=None, company=None, address=None,
                 home_tel=None, mob_tel=None, work_tel=None, fax_tel=None,
                 email=None, email2=None, email3=None, homepage_url=None,
                 bday=None, aday=None, bmonth=None, amonth=None, byear=None, ayear=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
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
        self.amonth = self.month_calc(amonth)
        self.bmonth = self.month_calc(bmonth)
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        # return "%s:%s:%s" % (self.id, self.last_name, self.first_name)
        return (f'\n____________________________________________________________________________________________'
                f'\n#####################################| id = {self.id} |###########################################'
                f'\nId= {self.id}'
                f'\nFirst name = {self.first_name} |Mid-name = {self.mid_name} |Last Name = {self.last_name} |'
                f'Nick = {self.nick_name} \nCompany = {self.company} |Address = {self.address}'
                f'\nH: {self.home_tel} |M: {self.mob_tel} |W: {self.work_tel} |F: {self.fax_tel} |'
                f'\nEmail = {self.email} |Email2 = {self.email2} |Email3 = {self.email3} |HPUrl = {self.homepage_url}'
                f'\nBorn_date = {self.bday}.{self.bmonth}.{self.byear} |'
                f'Anni_date = {self.aday}.{self.amonth}.{self.ayear}')
    # образец
    # #####################################| id = 950 |############################################
    # Id = 950
    # First name = 10 Фамилия |Mid-name = None |Last Name = Имя |Nick = None
    # Company = None |Address = 7777777 |строки с данными
    # H: None |M: None |W: None |F: None |
    # Email = None |Email2 = None |Email3 = None |HPUrl = None
    # Born_date = None.None.None |Anni_date = None.None.None |

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name
                and self.first_name == other.first_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def month_calc(self, month):
        try:
            if month is not None:
                month_list = ["January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December"]
                i = int(month) - 1
                month_name = month_list[i]
            else:
                month_name = None
        except:
            month_name = ""
        return month_name
