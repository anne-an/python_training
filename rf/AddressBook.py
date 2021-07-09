import json
import os
from fixture.application import Application
from fixture.db import DbFixture
from model.contact import Contact
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target["db"]
        self.db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                               password=db_config["password"])

    def destroy_fixtures(self):
        self.db_fixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.db_fixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def get_contact_list(self):
        return self.db_fixture.get_contact_list()

    def new_contact(self, firstname, middlename, lastname):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def modify_contact(self, contact, new_contact):
        self.fixture.contact.modify_contact_by_id(contact.id, new_contact)
