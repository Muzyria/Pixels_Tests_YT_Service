import time

import pytest

from pages_android.login_screen import LoginPage


class TestLoginPage:
    def test_login(self, request):
        print()
        print(f"START {request.node.name}")
        LoginPage().press_menu_button()
        # time.sleep(10)
        print(f"FINISH {request.node.name}")


