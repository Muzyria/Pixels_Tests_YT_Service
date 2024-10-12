import time

import pytest

from pages_android import LoginPage
from pages_android import CreateAccountPage
from pages_android import SelectCoursePage
from pages_android import SlideBarPage
from pages_android import LogOutPage

from pages_android import PendingApprovedPage


from common_test_steps import YamaTrackServiceScripts

from pages_android import Page

from framework_appium.driver_appium import DriverAppium

from credentials import EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER, EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN


@pytest.fixture(scope="class", autouse=True)
def check_login_option(request):
    if request.config.getoption("--login"):
        pytest.skip("Skipping tests because --login option is set")


class TestLoginPage:

    # @pytest.mark.parametrize("email, password", [(EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER),
    #                                              (EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)])

    @pytest.mark.admin
    def test_login_admin_valid_cred(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)

        assert PendingApprovedPage().is_pending_text_displayed(), "PENDING text is not displayed"
        assert PendingApprovedPage().is_approved_text_displayed(), "APPROVED text is not displayed"

        YamaTrackServiceScripts().logout_apk()

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
    def test_forgot_password(self, request):
        print()
        print(f"START {request.node.name}")

        # SelectCoursePage().press_slade_bar_button()
        # SlideBarPage().press_close_slade_bar_button()
        print("__________________________________________________________TEST_2")

        print(f"FINISH {request.node.name}")
