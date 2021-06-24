from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.create_if_no_contacts()
    app.contact.modify_first_contact(Contact(u"Олег", u"Олегович", u"Котиков", u"", "HR", "Auriga",
                                           u"Санкт-Петербург, Невский проспект, дом 99", "123456", "78998887766",
                                           "65432121", "123321",
                                           "oleg.kotikov@gmail.com", "6", "September", "1990", "3", "November", "1997"))
