import random
from random import randrange
from model.group import Group


def test_modify_some_group(app, db, check_ui):
    app.group.create_if_no_groups(db)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="qwerty", header="asdzxc123", footer="")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_name(app):
#     old_groups = app.group.get_group_list()
#     app.group.create_if_no_groups()
#     app.group.modify_first_group(Group(name="New group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.create_if_no_groups()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
