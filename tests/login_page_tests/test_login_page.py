import time

import pytest

from pages_android import LoginPage
from pages_android import CreateAccountPage
from pages_android import SelectCoursePage
from pages_android import SlideBarPage
from pages_android import LogOutPage

from common_test_steps import YamaTrackServiceScripts

from pages_android import Page

from framework_appium.driver_appium import DriverAppium

from credentials import EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER, EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN


@pytest.fixture(scope="class", autouse=True)
def check_login_option(request):
    if request.config.getoption("--login"):
        pytest.skip("Skipping tests because --login option is set")


class TestLoginPage:

    # def test_login_admin_valid_cred(self, request):
    #     print()
    #     print(f"START {request.node.name}")
    #
    #     LoginPage().login(EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)
    #
    #     print(f"FINISH {request.node.name}")

    def test_login_user_valid_cred(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER)
        YamaTrackServiceScripts.logout_apk()

        print(f"FINISH {request.node.name}")


    # @pytest.mark.skipif(not pytest.Config.getoption("--login"), reason="Skipping because --login is not set")
    # def test_second(self, request):
    #     print()
    #     print(f"START {request.node.name}")
    #
    #     # SelectCoursePage().press_slade_bar_button()
    #     # SlideBarPage().press_close_slade_bar_button()
    #
    #
    #     print(f"FINISH {request.node.name}")