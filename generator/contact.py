import jsonpickle
import os.path
import random
import string
from model.contact import Contact
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(firstname="", lastname="", middlename="", address="", home_phone="")] + [
    Contact(firstname=random_string("name", 10), lastname=random_string("lastname", 20),
            middlename=random_string("middlename", 15), address=random_string("address", 40),
            home_phone=random_string("homephone", 10), mobile_phone=random_string("mobphone", 10),
            work_phone=random_string("workphone", 10), email=random_string("email", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
