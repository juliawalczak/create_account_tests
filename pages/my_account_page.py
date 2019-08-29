from locators import locators
from selenium.webdriver.common.keys import Keys

class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = locators.MyAccountPageLocators.username_input
        self.password_input = locators.MyAccountPageLocators.password_input
        self.reg_email_input = locators.MyAccountPageLocators.reg_email_input
        self.reg_password_input = locators.MyAccountPageLocators.reg_password_input
        self.error_msg = locators.MyAccountPageLocators.error_msg
        self.logout_link = locators.MyAccountPageLocators.logout_link

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text