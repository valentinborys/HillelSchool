import pytest
from lecture_26.pages.RegistrationPage import RegistrationPage


@pytest.fixture
def setup():
    registration_page = RegistrationPage()
    yield registration_page
    registration_page.driver.quit()


def test_registration(setup):
    registration_page = setup
    registration_page.open_browser()
    registration_page.perform_registration_steps()
    registration_page.verify_registration_success()
