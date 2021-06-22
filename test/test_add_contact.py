# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(u"Олег", u"Олегович", u"Котиков", u"Котик", "HR", "Auriga",
                            u"Санкт-Петербург, Невский проспект, дом 100", "123456", "78998887766", "654321", "123321",
                            "oleg.kotikov@gmail.com", "6", "September", "1990"))
    app.logout()
