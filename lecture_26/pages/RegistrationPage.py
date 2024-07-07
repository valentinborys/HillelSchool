import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from lecture_26.pages.BasePage import BasePage
from lecture_26.locators.locators import Locators


class RegistrationPage(BasePage):
    def __init__(self, driver=None):
        if driver is None:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get("https://qauto2.forstudy.space/")
        pyautogui.write('guest')
        pyautogui.press('tab')
        pyautogui.write('welcome2qauto')
        pyautogui.press('enter')

    def open_browser(self):
        self.driver.get("https://qauto2.forstudy.space/")
        pyautogui.write('guest')
        pyautogui.press('tab')
        pyautogui.write('welcome2qauto')
        pyautogui.press('enter')

    def perform_registration_steps(self):
        self.element_is_clickable(Locators.SIGN_IN_BUTTON).click()
        self.element_is_clickable(Locators.REGISTRATION_BUTTON).click()
        self.element_is_visible(Locators.NAME_FIELD).send_keys("Valentyn")
        self.element_is_visible(Locators.LAST_NAME_FIELD).send_keys("Test")
        self.element_is_visible(Locators.EMAIL_FIELD).send_keys("valentyn123@test.com")
        self.element_is_visible(Locators.PASSWORD_FIELD).send_keys("123123Qwe")
        self.element_is_visible(Locators.RE_ENTER_PASSWORD_FIELD).send_keys("123123Qwe")
        self.element_is_clickable(Locators.REGISTER_BUTTON).click()

    def verify_registration_success(self):
        new_url = self.driver.current_url
        response = requests.get(new_url)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"

        garage_element = self.element_is_clickable(Locators.GARAGE)
        assert "Garage" == garage_element.text, "Expected text 'Garage', but got something else"