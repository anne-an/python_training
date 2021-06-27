# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    print(str(old_contacts))
    contact = Contact(u"Олег", u"Олегович", u"Котиков", u"Котик", "HR", "Auriga",
                               u"Санкт-Петербург, Невский проспект, дом 100", "123456", "78998887766", "654321",
                               "123321",
                               "oleg.kotikov@gmail.com", "6", "September", "1990", "", "-", "")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
