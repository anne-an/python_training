from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.accept_next_alert = True

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//form[@action='edit.php']").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_ddl_value(self, ddl_name, value):
        wd = self.app.wd
        if value:
            wd.find_element_by_name(ddl_name).click()
            Select(wd.find_element_by_name(ddl_name)).select_by_visible_text(value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_ddl_value("bday", contact.bday)
        self.change_ddl_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_ddl_value("aday", contact.aday)
        self.change_ddl_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.close_alert_and_get_its_text()
        wd.find_elements_by_class_name("msgbox")
        self.contact_cache = None

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_elements_by_link_text("Last name")
        if not len(wd.find_elements_by_link_text("Last name")) > 0:
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_link_text("Last name")

    def close_alert_and_get_its_text(self):
        wd = self.app.wd
        try:
            alert = wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_no_contacts(self):
        self.go_to_home_page()
        if self.count() == 0:
            self.create(Contact(firstname="Name"))

    contact_cache = None

    def get_contact_list(self):
        self.go_to_home_page()
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            table = wd.find_element_by_id("maintable")
            rows = table.find_elements_by_name("entry")
            for row in rows:
                ind = row.find_element_by_name("selected[]").get_attribute("value")
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                lastname = cells[1].text
                self.contact_cache.append(Contact(id=ind, firstname=name, lastname=lastname))
        return list(self.contact_cache)
