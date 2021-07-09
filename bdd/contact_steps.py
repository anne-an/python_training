import random
import pytest
from pytest_bdd import given, when, then
from model.contact import Contact


@pytest.fixture
@given("a contact list")
def contact_list(db):
    return db.get_contact_list()


@pytest.fixture
@given("a contact with <firstname>, <middlename> and <lastname>")
def new_contact(firstname, middlename, lastname):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname)


@pytest.fixture
@when("I add the contact to the list")
def add_new_contact(app, new_contact, db):
    app.contact.create(new_contact)
    return db.get_contact_list()


@pytest.fixture
@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, contact_list, new_contact, add_new_contact):
    old_contacts = contact_list
    new_contacts = add_new_contact
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@pytest.fixture
@given("a non-empty contact list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="some name"))
    return db.get_contact_list()


@pytest.fixture
@given("a contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@pytest.fixture
@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@pytest.fixture
@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deletion(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@pytest.fixture
@when("I modify contact information")
def modify_contact(app, random_contact, new_contact):
    app.contact.modify_contact_by_id(random_contact.id, new_contact)


@pytest.fixture
@then("the new contact list is equal to the old one with the modified contact")
def verify_contact_modification(db, non_empty_contact_list, random_contact, new_contact, check_ui, app):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    index = old_contacts.index(random_contact)
    old_contacts[index] = new_contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
