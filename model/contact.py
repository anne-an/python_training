from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, email=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, id=None, secondary_phone=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return maxsize

