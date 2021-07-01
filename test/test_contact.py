from random import randrange


def test_contact_on_edit_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == contact_from_edit_page.all_emails_from_home_page
    assert contact_from_home_page.all_phones_from_home_page == contact_from_edit_page.all_phones_from_home_page


def test_contact_in_db(app, db):
    ids = db.get_all_contact_ids()
    for id in ids:
        contact_from_home_page = app.contact.get_contact_by_id(id)
        contact_from_db = db.get_contact_by_id(id)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emails_from_home_page == contact_from_db.all_emails_from_home_page
        assert contact_from_home_page.all_phones_from_home_page == contact_from_db.all_phones_from_home_page
