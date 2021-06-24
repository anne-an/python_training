from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="qwerty", header="asdzxc123", footer=""))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
