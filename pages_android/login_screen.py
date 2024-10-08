import time

from pages_android import Page



class LoginPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    LOGIN_IN_BUTTON = ("xpath", "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")



    # def check_menu_button_is_visible(self) -> bool:
    #     self.visibility_of_element_located(self.MENU_BUTTON_ID)
    #     return True

    def press_menu_button(self) -> "LoginPage":
        self.presence_of_element_located(self.LOGIN_IN_BUTTON).click()
        return self



