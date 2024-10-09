import time

from pages_android import Page


class LoginPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    EMAIL_INPUT_FIELD = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
    PASSWORD_INPUT_FIELD = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")

    LOGIN_IN_BUTTON = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")

    def login(self):
        self.presence_of_element_located(self.EMAIL_INPUT_FIELD).send_keys("123")
        self.presence_of_element_located(self.PASSWORD_INPUT_FIELD).send_keys("123")
        self.presence_of_element_located(self.LOGIN_IN_BUTTON).click()

    def press_login_button(self) -> "LoginPage":
        self.presence_of_element_located(self.LOGIN_IN_BUTTON).click()
        return self



