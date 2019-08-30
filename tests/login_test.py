import pytest
import allure
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Test: account login with valid data")
    @allure.description("Inputting valid email address and password. Checking if the user has been logged in.")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython")

        assert my_account_page.is_logout_link_displayed()

    @allure.title("Test: account login with invalid data")
    @allure.description("Inputting valid email address and invalid password. Checking an error message.")
    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython123")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()