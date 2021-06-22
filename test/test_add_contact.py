# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(u"Олег", u"Олегович", u"Котиков", u"Котик", "HR", "Auriga",
                               u"Санкт-Петербург, Невский проспект, дом 100", "123456", "78998887766", "654321",
                               "123321",
                               "oleg.kotikov@gmail.com", "6", "September", "1990", "", "", ""))
    app.session.logout()
