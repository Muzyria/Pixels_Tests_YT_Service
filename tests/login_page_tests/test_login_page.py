import time

import pytest

from pages_android.login_screen import LoginPage
from pages_android.create_account_screen import CreateAccountPage

from pages_android import Page


class TestLoginPage:
    def test_login(self, request):
        print()
        print(f"START {request.node.name}")

        LoginPage().press_create_account_button()
        CreateAccountPage.swipe()

        CreateAccountPage().press_submit_button()


        time.sleep(3)

        print("TEST_______________________")
        print(f"FINISH {request.node.name}")


