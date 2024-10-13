from faker import Faker

from pages_android import SlideBarPage, LogOutPage


class YamaTrackServiceScripts:
    @staticmethod
    def logout_apk():
        SlideBarPage().press_slade_bar_button().press_logout_button()
        LogOutPage().press_logout_button()


class Generator:
    @staticmethod
    def get_fake_email():
        return Faker().email()

    @staticmethod
    def get_fake_password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True):
        password = Faker().password(length=length,
                                    special_chars=special_chars,
                                    digits=digits,
                                    upper_case=upper_case,
                                    lower_case=lower_case)
        return password


if __name__ == '__main__':
    print(Generator().get_fake_email())
    print(Generator().get_fake_password(special_chars=False))
