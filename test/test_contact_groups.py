import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    app.group.create_if_no_groups(orm)
    app.contact.create_if_no_contacts(orm)
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.create(Contact(firstname="Name"))
        contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)
    old_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact in new_contacts_in_group
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)


def test_delete_contact_from_group(app, orm):
    app.group.create_if_no_groups(orm)
    app.contact.create_if_no_contacts(orm)
    groups_with_contacts = orm.get_not_empty_groups()
    if len(groups_with_contacts) == 0:
        rand_group = random.choice(orm.get_group_list())
        rand_contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group_by_id(rand_contact.id, rand_group.name)
        groups_with_contacts = orm.get_not_empty_groups()
    group = random.choice(groups_with_contacts)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contacts_in_group
