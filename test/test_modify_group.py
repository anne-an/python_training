from random import randrange
from model.group import Group


def test_modify_some_group(app):
    app.group.create_if_no_groups()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="qwerty", header="asdzxc123", footer="")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
