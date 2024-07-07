# page_objects/registration_page.py
from lecture_26.locators.locators import Locators
from lecture_26.pages.BasePage import BasePage


class RegistrationPage(BasePage):
    def get_sigh_in_button(self):
        return self.find_element(*Locators.SIGN_IN_BUTTON)

    def get_email_button(self):
        return self.find_element(*Locators.EMAIL_BUTTON)

    def get_registration_button(self):
        return self.find_element(*Locators.REGISTRATION_BUTTON)

    def get_login_button(self):
        return self.find_element(*Locators.LOGIN_BUTTON)

    def get_name_field(self):
        return self.find_element(*Locators.NAME_FIELD)

    def get_last_name_field(self):
        return self.find_element(*Locators.LAST_NAME_FIELD)

    def get_email_field(self):
        return self.find_element(*Locators.EMAIL_FIELD)

    def get_re_enter_password_field(self):
        return self.find_element(*Locators.RE_ENTER_PASSWORD_FIELD)
