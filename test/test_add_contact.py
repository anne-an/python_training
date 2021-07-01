# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Contact(firstname=name, lastname=lastname, middlename="Отчество",
            address=address, home_phone=home_phone, mobile_phone="89879879877",
            work_phone="654321", email=email)
    for name in ["", random_string("name", 10)]
    for lastname in ["", random_string("lastname", 20)]
    for address in ["", random_string("address", 20)]
    for home_phone in ["", random_string("home_phone", 20)]
    for email in ["", random_string("email", 20)]
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
