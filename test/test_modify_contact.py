from model.contact import Contact


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_if_no_contacts()
    contact = Contact(u"Олег", u"Олегович", u"Котиков", u"", "HR", "Auriga",
                                           u"Санкт-Петербург, Невский проспект, дом 99", "123456", "78998887766",
                                           "65432121", "123321",
                                           "oleg.kotikov@gmail.com", "6", "September", "1990", "3", "November", "1997")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
