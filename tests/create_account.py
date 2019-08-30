import pytest
import random
import allure
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @allure.title("Test: create an account with invalid data.")
    @allure.description("Inputting already register email address and password. Checking for an error message.")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython")

        msg = 'An account is already register with your email address. Please log in.'
        assert msg in my_account_page.get_error_msg()

    @allure.title("Test: create an account with valid data.")
    @allure.description("Inputting valid email address and password. Checking if an account will be created.")
    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + "testeroprogramowaniapython@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "testeroprogramowaniapython")

        assert my_account_page.is_logout_link_displayed()
