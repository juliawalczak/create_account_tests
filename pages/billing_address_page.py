from locators.locators import BillingAddressLocators
from selenium.webdriver.support.select import Select
import logging

class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.adresses_link = BillingAddressLocators.adresses_link
        self.edit_link = BillingAddressLocators.edit_link
        self.country_select = BillingAddressLocators.country_select
        self.adresses_input = BillingAddressLocators.adresses_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_adress_button = BillingAddressLocators.save_adress_button
        self.msg_div = BillingAddressLocators.message_div

    def open_edit_billing_address(self):
        logging.info("Opening edit billing address page")
        self.driver.find_element(*self.adresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, first_name, last_name):
        logging.info("Setting first name: {} and last name: {}".format(first_name, last_name))
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def select_country(self, country):
        logging.info("Setting country: {}".format(country))
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        logging.info("Setting street: {}, postcode: {}, city: {}".format(street, postcode, city))
        self.driver.find_element(*self.adresses_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        logging.info("Setting phone number: {}".format(number))
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_address(self):
        logging.info("Saving billing address")
        self.driver.find_element(*self.save_adress_button).click()

    def get_message_text(self):
        logging.info("Getting message")
        return self.driver.find_element(*self.msg_div).text