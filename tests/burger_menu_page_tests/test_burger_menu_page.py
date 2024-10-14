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


class TestBurgerMenuPage:
    @pytest.mark.user
    def test_burger_menu_user(self, request):
        """
        1. Press / Unpress to Burger menu button and Confirm sidebar menu is opened /closed
        2. Check and confirm Sidebar has next items with described behavior
        - user name in title - after clicking My account screen is opened
        - email address - after clicking My account screen is opened
        3. CARS:
        - If the course is not selected - after clicking CARS button SELECT COURSE screen is opened
        - If the course is not selected - after clicking CARS SELECTED COURSE screen is opened with the car list
        4. MY ACCOUNT - after clicking MY ACCOUNT MY ACCOUNT screen is opened
        5. HELP - after clicking HELP - Need Help? screen is opened
        6. LOGOUT - after clicking LOGOUT screen is opened
        """
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER)
        SlideBarPage().press_slade_bar_button()

        for item in ["Alexander Muzyria", EMAIL_SERVICE_USER, "CARS", "MY ACCOUNT", "HELP", "LOGOUT"]:
            assert SlideBarPage().is_object_displayed(item)

        SlideBarPage().press_close_slade_bar_button()

        print(f"FINISH {request.node.name}")

    @pytest.mark.admin
    def test_burger_menu_admin(self, request):
        """
        1. Press / Unpress to Burger menu button and Confirm sidebar menu is opened /closed
        2. Check and confirm Sidebar has next items with described behavior:
        - user name in title - after clicking My account screen is opened
        - email address - after clicking My account screen is opened

        3. CARS:
        - If the course is not selected - after clicking CARS button SELECT COURSE screen is opened
        - If the course is not selected - after clicking CARS SELECTED COURSE screen is opened with car list
        4. ADMIN TOOLS has counter with amount of Pending list - after click previously Pending (or Approved) list is opened (It’s expected)
        5. MY ACCOUNT - after clicking MY ACCOUNT MY ACCOUNT screen is opened
        6. HELP - after clicking HELP - Need Help? screen is opened (Screen attached)
        7. LOGOUT - after clicking LOGOUT screen is opened
        """
        print()
        print(f"START {request.node.name}")

        LoginPage().login(EMAIL_SERVICE_ADMIN, PASSWORD_SERVICE_ADMIN)
        SlideBarPage().press_slade_bar_button()

        # for item in ["Alexander Muzyria", EMAIL_SERVICE_USER, "CARS", "MY ACCOUNT", "HELP", "LOGOUT"]:
        #     assert SlideBarPage().is_object_displayed(item)

        # SlideBarPage().press_close_slade_bar_button()

        print(f"FINISH {request.node.name}")

