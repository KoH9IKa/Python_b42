# -*- coding: utf-8 -*-
from model.contact_info import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

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
               + string.ascii_letters * 5 + string.digits * 5 + "." * 5 + "-" * 5 + " " * 2)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + "," * 3 + " " * 2
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


def random_day(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_month(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_year(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=random_names("name", 10),
                    mid_name=random_names("midname", 10),
                    last_name=random_names("lastname", 10),
                    address=random_address(10),
                    mob_tel=random_phone("+7", 10),
                    work_tel=random_phone("+7", 10),
                    home_tel=random_phone("+7", 10),
                    fax_tel=random_phone("+7", 10),
                    email=random_email(20),
                    email2=random_email(20),
                    email3=random_email(20))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    out.write(jsonpickle.encode(testdata))
