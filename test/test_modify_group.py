from model.group import Group


def test_modify_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_if_no_groups()
    group = Group(name="qwerty", header="asdzxc123", footer="")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
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
