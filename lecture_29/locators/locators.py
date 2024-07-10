from selenium.webdriver.common.by import By


class Locators:
    SIGN_IN_BUTTON = (By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    REGISTRATION_BUTTON = (By.XPATH, "//*[text()='Registration']")
    NAME_FIELD = (By.ID, "signupName")
    LAST_NAME_FIELD = (By.ID, "signupLastName")
    EMAIL_FIELD = (By.ID, "signupEmail")
    PASSWORD_FIELD = (By.ID, "signupPassword")
    RE_ENTER_PASSWORD_FIELD = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//*[@class='btn btn-primary']")
    GARAGE = (By.XPATH, "(//*[text()='Garage'])[1]")

