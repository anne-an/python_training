def test_delete_first_group(app):
    app.group.create_if_no_groups()
    app.group.delete_first_group()
