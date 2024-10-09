import time

import pytest

from pages_android.login_screen import LoginPage


class TestLoginPage:
    def test_login(self, request):
        print()
        print(f"START {request.node.name}")
        # LoginPage().press_login_button()
        time.sleep(10)
        print("TEST_______________________")
        print(f"FINISH {request.node.name}")


