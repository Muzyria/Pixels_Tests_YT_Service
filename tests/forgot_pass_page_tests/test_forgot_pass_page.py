import time

import pytest

from pages_android import LoginPage
from pages_android import CreateAccountPage
from pages_android import SelectCoursePage
from pages_android import SlideBarPage
from pages_android import LogOutPage
from pages_android import ForgotPasswordPage

from pages_android import PendingApprovedPage


from common_test_steps import YamaTrackServiceScripts, Generator

from pages_android import Page

from framework_appium.driver_appium import DriverAppium

from credentials import EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER, EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN


@pytest.fixture(scope="class", autouse=True)
def check_login_option(request):
    if request.config.getoption("--login"):
        pytest.skip("Skipping tests because --login option is set")


@pytest.mark.skip
class TestForgotPassPage:

    def test_forgot_password(self, request):
        """
        Case A:Forgot Password
        1. Open Log in screen and press to [Forgot Password] button
        2. Compare and confirm Forgot Password screen matching to design
        3. Leave email address blank then press [Submit] button - confirm error message “Please enter the valid Email address”
        4. Enter non-existent email address then press [Submit] button confirm error message “No user found"
        5. Enter valid Email address then press [Submit] button - confirm Forgot Password infoscreen is opened.
        6. Press [Close] button on Thank you screen - Confirm Log in screen is opened
        7. Click to back button and confirm Log in screen is opened
        """
        print()
        print(f"START {request.node.name}")
        # step 1
        LoginPage().press_forgot_password()
        # step 2
        ForgotPasswordPage().is_forgot_password_text_displayed()
        # step 3
        ForgotPasswordPage().enter_email_for_password("")
        ForgotPasswordPage().press_submit_button()

        alert_text = ForgotPasswordPage().is_alert_displayed("Please enter the email address")
        assert alert_text == "Please enter the email address", "Alert 'Please enter the email address' is not displayed"

        # step 4
        ForgotPasswordPage().enter_email_for_password(Generator.get_fake_email())
        ForgotPasswordPage().press_submit_button()

        alert_text = ForgotPasswordPage().is_alert_displayed("No user found")
        print(alert_text)
        assert alert_text == "No user found", "Alert 'No user found' is not displayed"

        print(f"FINISH {request.node.name}")

    def test_forgot_password_2(self, request):
        print()
        print(f"START {request.node.name}")
        # step 5
        LoginPage().press_forgot_password()
        ForgotPasswordPage().enter_email_for_password(EMAIL_SERVICE_USER)
        ForgotPasswordPage().press_submit_button()
        ForgotPasswordPage().press_close_button()

        print(f"FINISH {request.node.name}")


