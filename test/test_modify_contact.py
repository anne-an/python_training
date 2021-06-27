from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.create_if_no_contacts()
    contact = Contact(u"Олег", u"Олегович", u"Котиков", u"", "HR", "Auriga",
                                           u"Санкт-Петербург, Невский проспект, дом 99", "123456", "78998887766",
                                           "65432121", "123321",
                                           "oleg.kotikov@gmail.com", "6", "September", "1990", "3", "November", "1997")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
