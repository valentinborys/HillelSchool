import time
import allure
import pytest
import requests
from lecture_29.locators.locators import Locators
from lecture_29.pages.RegistrationPage import RegistrationPage


@pytest.fixture
def setup():
    registration_page = RegistrationPage()
    yield registration_page
    registration_page.driver.quit()


@allure.feature("Registration checking")
@allure.step("Пошук та взаємодія з основними елементами")
def test_registration(setup):
    registration_page = setup
    registration_page.element_is_clickable(Locators.SIGN_IN_BUTTON).click()
    registration_page.element_is_clickable(Locators.REGISTRATION_BUTTON).click()
    registration_page.element_is_visible(Locators.NAME_FIELD).send_keys("Valentyn")
    registration_page.element_is_visible(Locators.LAST_NAME_FIELD).send_keys("Test")
    registration_page.element_is_visible(Locators.EMAIL_FIELD).send_keys("biр1fdg1f12123gehgins@from.shir")
    registration_page.element_is_visible(Locators.PASSWORD_FIELD).send_keys("123123Qwe")
    registration_page.element_is_visible(Locators.RE_ENTER_PASSWORD_FIELD).send_keys("123123Qwe")
    registration_page.element_is_clickable(Locators.REGISTER_BUTTON).click()

    new_url = registration_page.driver.current_url
    response = requests.get(new_url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    garage_element = registration_page.element_is_clickable(Locators.GARAGE)
    assert "Garage" == garage_element.text, "Expected text 'Garage', but got something else"
