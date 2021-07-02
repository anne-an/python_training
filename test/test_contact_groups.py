import random
from model.group import Group


def test_add_contact_to_group(app, orm):
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    group = random.choice(groups)
    app.contact.add_to_group_by_id(contact.id, group.name)
    contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact in contacts_in_group


def test_delete_contact_from_group(app, orm):
    groups_with_contacts = orm.get_not_empty_groups()
    group = random.choice(groups_with_contacts)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contacts_in_group
