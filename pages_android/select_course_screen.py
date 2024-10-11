import time

from pages_android import Page


class SelectCoursePage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    COURSE_INPUT_FIELD = ("xpath", '//android.widget.EditText')
    NEXT_BUTTON = ("xpath", '//android.widget.TextView[@text="NEXT"]')
    HELP_BUTTON = ("xpath", '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView')

    def enter_select_course_field(self, name_course: str):
        self.presence_of_element_located(self.COURSE_INPUT_FIELD).send_keys(name_course)

    def press_next_button(self):
        self.presence_of_element_located(self.NEXT_BUTTON).click()






