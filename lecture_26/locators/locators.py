import driver
from selenium.webdriver.common.by import By


class Locators:
    # Main page
    SIGN_IN_BUTTON = (By.XPATH, "//*[@class='btn btn-outline-white header_signin']")

    # Log in pop-up
    EMAIL_BUTTON = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[1]"
    PASSWORD_BUTTON = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[2]"
    REGISTRATION_BUTTON = "//*[text()='Registration']"
    LOGIN_BUTTON = "//*[text()='Login']"

    # Registration pop-up
    NAME_FIELD = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[1]"
    LAST_NAME_FIELD = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[2]"
    EMAIL_FIELD = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[3]"
    PASSWORD_FIELD = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[4]"
    RE_ENTER_PASSWORD_FIELD = "(//*[@class='form-control ng-untouched ng-pristine ng-invalid'])[5]"
