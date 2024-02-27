# -*- coding: utf-8 -*-
from model.contact_info import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

RANDOM_DAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 30, "-", ""]
RANDOM_MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December', "-"]
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_names(prefix, maxlen):
    symbols = ("йцукенгшщзхъфывапролджэячсмитьбю"
               + string.ascii_letters * 5 + string.digits * 5 + "." * 5 + "-" * 5)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + "," * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits + "@" * 5 + "." * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_url(maxlen):
    symbols = string.ascii_letters + string.digits + "." * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return random.choice(RANDOM_DAY)


def random_month():
    return random.choice(RANDOM_MONTH)


def random_year(maxlen):
    return "".join([random.choice(string.digits) for i in range(4)])


testdata = [Contact(first_name=random_names("name", 10),
                    mid_name=random_names("midname", 10),
                    last_name=random_names("lastname", 10),
                    nick_name=random_names("nickname", 10),
                    company=random_names("company", 10),
                    title=random_names("title", 10),
                    address=random_address(10),
                    mob_tel=random_phone("+7", 10),
                    work_tel=random_phone("+7", 10),
                    home_tel=random_phone("+7", 10),
                    fax_tel=random_phone("+7", 10),
                    email=random_email(20),
                    email2=random_email(20)
                    , email3=random_email(20)
                    , homepage_url=random_url(40)
                    , bday=random_day()
                    , bmonth=random_month()
                    , byear=random_year(4)
                    , aday=random_day()
                    , amonth=random_month()
                    , ayear=random_year(4)
                    )
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    out.write(jsonpickle.encode(testdata))
