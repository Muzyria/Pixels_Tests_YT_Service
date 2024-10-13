import time

from pages_android import Page


class ForgotPasswordPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    FORGOT_PASSWORD_TEXT = ('xpath', '//android.widget.TextView[@text="FORGOT PASSWORD"]')

    EMAIL_INPUT_FIELD = ("xpath", '//android.widget.EditText')
    SUBMIT_BUTTON = ("xpath", '//android.widget.TextView[@text="SUBMIT"]')
    BACK_BUTTON = ("xpath", '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')

    def is_forgot_password_text_displayed(self):
        return self.visibility_of_element_located(self.FORGOT_PASSWORD_TEXT).is_displayed()

    def press_back_button(self):
        self.visibility_of_element_located(self.BACK_BUTTON).click()

