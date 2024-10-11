import time

import pytest

from pages_android import LoginPage
from pages_android import CreateAccountPage
from pages_android import SelectCoursePage
from pages_android import SlideBarPage
from pages_android import LogOutPage

from pages_android import Page


class TestLoginPage:
    def test_login(self, request):
        print()
        print(f"START {request.node.name}")

        SelectCoursePage().press_slade_bar_button()
        SlideBarPage().press_close_slade_bar_button()

        SelectCoursePage().press_slade_bar_button()
        SlideBarPage().press_logout_button()
        LogOutPage().press_cancel_button()

        SelectCoursePage().press_slade_bar_button()
        SlideBarPage().press_logout_button()

        LogOutPage().press_logout_button()


        print(f"FINISH {request.node.name}")


