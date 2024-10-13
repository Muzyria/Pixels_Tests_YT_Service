import time

from pages_android import Page


class LogOutPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    CANCEL_BUTTON = ("xpath", '//android.widget.TextView[@text="CANCEL"]')
    # LOGOUT_BUTTON = ("xpath", '//android.widget.TextView[@text="LOG OUT"]')
    LOGOUT_BUTTON = ("xpath", '//android.view.ViewGroup[3]')

    def press_cancel_button(self):
        self.presence_of_element_located(self.CANCEL_BUTTON).click()

    def press_logout_button(self):
        print("CLICK LOG OUT BUTTON")
        time.sleep(1)
        self.element_to_be_clickable(self.LOGOUT_BUTTON).click()
