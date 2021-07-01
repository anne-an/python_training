import re

import pymysql
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_all_contact_ids(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from addressbook where deprecated='0000-00-00 00:00:00'")
            for id in cursor.fetchall():
                list.append(id[0])
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, "
                           "phone2 from addressbook where id=%s" % id)
            contact_info = cursor.fetchall()[0]
            (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = contact_info
            contact = Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                              all_emails_from_home_page="\n".join(filter(lambda x: x != "", [email, email2, email3])),
                              all_phones_from_home_page=self.merge_phones(home, mobile, work, phone2))
        finally:
            cursor.close()
        return contact

    def merge_phones(self, home, mobile, work, phone2):
        def clear(s):
            return re.sub("[() -]", "", s)

        return "\n".join(filter(lambda x: x != "",
            map(lambda x: clear(x),
                filter(lambda x: x is not None,
                       [home, mobile, work, phone2]))))

    def destroy(self):
        self.connection.close()
