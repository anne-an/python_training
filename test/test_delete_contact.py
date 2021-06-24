def test_delete_first_contact(app):
    app.contact.create_if_no_contacts()
    app.contact.delete_first_contact()
