import time

from credentials import EMAIL_SERVICE_USER, PASSWORD_SERVICE_USER
from pages_android import Page


class LoginPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    EMAIL_INPUT_FIELD = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
    PASSWORD_INPUT_FIELD = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")

    LOGIN_IN_BUTTON = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")

    FORGOT_PASSWORD_BUTTON = ("xpath", '//android.widget.TextView[@text="Forgot Password?"]')
    CREATE_NEW_USER_BUTTON = ("xpath", '//android.widget.TextView[@text="CREATE NEW USER ACCOUNT"]')


    ALERT_ENTER_REGISTER_EMAIL = ("xpath", '//*[contains(@text, "Please enter your registered email")]')
    ALERT_ENTER_VALID_EMAIL = ("xpath", '//*[contains(@text, "Please enter the valid Email Address")]')

    ALERT_ENTER_PASSWORD = ("xpath", '//*[contains(@text, "Please enter password to continue")]')
    ALERT_AUTH_FAILED = ("xpath", '//*[contains(@text, "Authentication failed.")]')

    def login(self, login: str = EMAIL_SERVICE_USER, password: str = PASSWORD_SERVICE_USER):
        self.presence_of_element_located(self.EMAIL_INPUT_FIELD).send_keys(login)
        self.presence_of_element_located(self.PASSWORD_INPUT_FIELD).send_keys(password)
        self.presence_of_element_located(self.LOGIN_IN_BUTTON).click()

    def enter_email_field(self, email: str):
        self.presence_of_element_located(self.EMAIL_INPUT_FIELD).send_keys(email)

    def enter_password_field(self, password: str):
        self.presence_of_element_located(self.PASSWORD_INPUT_FIELD).send_keys(password)

    def press_login_button(self):
        self.presence_of_element_located(self.LOGIN_IN_BUTTON).click()

    #-------------------------------------------------------------------------------------------------------------------

    def press_forgot_password(self):
        self.visibility_of_element_located(self.FORGOT_PASSWORD_BUTTON).click()

    def press_create_account_button(self):
        self.presence_of_element_located(self.CREATE_NEW_USER_BUTTON).click()

    def is_alert_displayed(self, text):
        locator = ("xpath", f'//*[contains(@text, "{text}")]')

        return self.presence_of_element_located(self.ALERT_AUTH_FAILED).is_displayed()
