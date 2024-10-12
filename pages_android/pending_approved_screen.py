import time

from pages_android import Page


class PendingApprovedPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ""

    PENDING_TEXT = ("xpath", '//android.widget.TextView[@text="PENDING"]')
    APPROVED_TEXT = ("xpath", '//android.widget.TextView[@text="APPROVED"]')

    def is_pending_text_displayed(self):
        return self.visibility_of_element_located(self.PENDING_TEXT).is_displayed()

    def is_approved_text_displayed(self):
        return self.visibility_of_element_located(self.APPROVED_TEXT).is_displayed()
