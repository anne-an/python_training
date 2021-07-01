import random
from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    app.contact.create_if_no_contacts(db)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = Contact(firstname="Олег", middlename="Олегович", lastname="Котиков", nickname="",
                          title="HR", company="Auriga", address="Санкт-Петербург, Невский проспект, дом 99",
                          home_phone="123456", mobile_phone="78998887766", work_phone="65432121", fax = "123321",
                          email="oleg.kotikov@gmail.com", bday="6", bmonth="September", byear="1990",
                          aday="3", amonth="November", ayear="1997")
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
