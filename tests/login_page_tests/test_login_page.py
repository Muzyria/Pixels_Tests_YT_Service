import time

import pytest

from pages_android.login_screen import LoginPage

from pages_android import Page


class TestLoginPage:
    def test_login(self, request):
        print()
        print(f"START {request.node.name}")
        # LoginPage().press_login_button()

        print()

        print(Page.get_name_current_activity())
        time.sleep(5)

        print("TEST_______________________")
        print(f"FINISH {request.node.name}")


