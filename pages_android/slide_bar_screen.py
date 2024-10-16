import time

from pages_android import Page


class SlideBarPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    CLOSE_SLIDE_BAR = ("xpath", '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')

    NAME_USER_BUTTON = ('xpath', '//android.widget.TextView[@text="Alexander Muzyria"]')
    EMAIL_BUTTON = ('xpath', '//android.widget.TextView[@text="alexander.muzyria@pixelsmatter.com"]')
    CARS_BUTTON = ("xpath", '//android.widget.TextView[@text="CARS"]')
    MY_ACCOUNT_BUTTON = ("xpath", '//android.widget.TextView[@text="MY ACCOUNT"]')
    HELP_BUTTON = ("xpath", '//android.widget.TextView[@text="HELP"]')
    LOGOUT_BUTTON = ("xpath", '//android.widget.TextView[@text="LOGOUT"]')

    SLIDE_BAR_BUTTON = ("xpath", '//android.view.ViewGroup[2]/android.widget.ImageView')

    def press_slade_bar_button(self):
        self.visibility_of_element_located(self.SLIDE_BAR_BUTTON).click()
        return self

    def press_close_slade_bar_button(self):
        self.presence_of_element_located(self.CLOSE_SLIDE_BAR).click()

    def press_logout_button(self):
        self.presence_of_element_located(self.LOGOUT_BUTTON).click()

    # ------------------------------------------------------------------------------------------------------------------
    def is_object_displayed(self, name_text: str):
        locator = ("xpath", f'//android.widget.TextView[@text="{name_text}"]')
        print(locator)
        return self.visibility_of_element_located(locator).is_displayed()



