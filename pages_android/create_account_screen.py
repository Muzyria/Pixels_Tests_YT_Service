import time

from pages_android import Page


class CreateAccountPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""


    CREATE_ACCOUNT_TEXT = ('xpath', '//android.widget.TextView[@text="CREATE ACCOUNT"]')

    FIRST_NAME_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText')
    LAST_NAME_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText')
    EMAIL_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText')
    COMPANY_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.EditText')
    PASSWORD_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText')
    CONFIRM_PASSWORD_INPUT_FIELD = ("xpath", '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText')

    SUBMIT_BUTTON = ("xpath", '//android.widget.TextView[@text="SUBMIT"]')

    BACK_BUTTON = ("xpath", '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')


    def is_create_account_text_displayed(self):
        return self.visibility_of_element_located(self.CREATE_ACCOUNT_TEXT).is_displayed()

    def is_submit_button_displayed(self):
        return self.visibility_of_element_located(self.SUBMIT_BUTTON).is_displayed()


    def press_submit_button(self):
        self.presence_of_element_located(self.SUBMIT_BUTTON).click()


    def press_back_button(self):
        self.presence_of_element_located(self.BACK_BUTTON).click()

