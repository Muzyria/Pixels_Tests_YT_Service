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


class TestLoginPage:

    @pytest.mark.admin
    def test_login_admin_valid_cred(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)

        assert PendingApprovedPage().is_pending_text_displayed(), "PENDING text is not displayed"
        assert PendingApprovedPage().is_approved_text_displayed(), "APPROVED text is not displayed"

        YamaTrackServiceScripts().logout_apk()

        print(f"FINISH {request.node.name}")

    @pytest.mark.admin
    def test_log_out_admin(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)

        SlideBarPage().press_slade_bar_button().press_logout_button()
        LogOutPage().press_cancel_button()

        YamaTrackServiceScripts.logout_apk()

        print(f"FINISH {request.node.name}")

    @pytest.mark.user
    def test_login_user_valid_cred(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER)

        assert SelectCoursePage().is_select_course_text_displayed(), "SELECT COURSE text is not displayed"
        assert SelectCoursePage().is_select_course_field_displayed(), "SELECT COURSE field is not displayed"

        YamaTrackServiceScripts.logout_apk()

        print(f"FINISH {request.node.name}")

    @pytest.mark.user
    def test_forgot_pass_screen(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().press_forgot_password()

        assert ForgotPasswordPage().is_forgot_password_text_displayed()

        ForgotPasswordPage().press_back_button()

        print(f"FINISH {request.node.name}")

    @pytest.mark.user
    def test_create_new_user_account_screen(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().press_create_account_button()

        assert CreateAccountPage().is_create_account_text_displayed()
        CreateAccountPage.swipe()
        assert CreateAccountPage().is_submit_button_displayed()
        CreateAccountPage.swipe(500, 200, 500, 700, 250)

        CreateAccountPage().press_back_button()

        print(f"FINISH {request.node.name}")

    @pytest.mark.user
    def test_log_out_user(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER)

        SlideBarPage().press_slade_bar_button().press_logout_button()
        LogOutPage().press_cancel_button()

        YamaTrackServiceScripts.logout_apk()

        print(f"FINISH {request.node.name}")

    @pytest.mark.user
    @pytest.mark.parametrize("email, password, expected",
                             [(Generator.get_fake_email(), Generator.get_fake_password(), "Authentication failed."),
                              (EMAIL_SERVICE_USER, Generator.get_fake_password(), "Authentication failed."),
                              (Generator.get_fake_email(), PASSWORD_SERVICE_USER, "Authentication failed."),
                              ('', Generator.get_fake_password(), "Please enter your registered email"),
                              (Generator.get_fake_email(), '', "Please enter password to continue"),
                              ('', '', "Please enter your registered email")])
    def test_incorrect_cred(self, request, email, password, expected):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(email, password)

        alert_text = LoginPage().is_alert_displayed(expected)
        assert alert_text == expected, f"Alert {expected} is not displayed"

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().press_forgot_password()
        ForgotPasswordPage().enter_email_for_password(EMAIL_SERVICE_USER)

        ForgotPasswordPage().press_submit_button()

        ForgotPasswordPage().press_close_button()

        print(f"FINISH {request.node.name}")


