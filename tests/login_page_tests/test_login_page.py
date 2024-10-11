import time

import pytest

from pages_android import LoginPage
from pages_android import CreateAccountPage
from pages_android import SelectCoursePage
from pages_android import SlideBarPage
from pages_android import LogOutPage

from pages_android import Page

from framework_appium.driver_appium import DriverAppium


class TestLoginPage:

    # @pytest.mark.skipif(pytest.config.getoption("login"), reason="Skipping because --login is set")


    def test_login(self, request):
        print()
        print(f"START {request.node.name}")

        # conf = pytest.Config.getoption("--login")
        # print(conf)

        # SelectCoursePage().press_slade_bar_button()
        # SlideBarPage().press_close_slade_bar_button()
        #
        # SelectCoursePage().press_slade_bar_button()
        # SlideBarPage().press_logout_button()
        # LogOutPage().press_cancel_button()
        #
        # SelectCoursePage().press_slade_bar_button()
        # SlideBarPage().press_logout_button()
        #
        # LogOutPage().press_logout_button()

        # LoginPage().enter_email_field("qwe@sd.tu")
        # LoginPage().enter_password_field("123")
        # LoginPage().press_login_button()
        # time.sleep(1)
        #
        # try:
        #     alert = (DriverAppium.appium_instance.find_element("xpath", '//*[contains(@text, "Au")]'))
        #     print(alert.text)
        # except Exception:
        #     print("Всплывающее сообщение не найдено")
        #
        # print(f"FINISH {request.node.name}")


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