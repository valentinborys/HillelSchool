import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
from lecture_26.pages import BasePage
from lecture_26.pages import RegistrationPage

from lecture_26 import locators
from lecture_26.locators.locators import Locators


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_prompt_alert(driver):
    url = "https://qauto2.forstudy.space/"
    driver.get(url)
    driver.maximize_window()

    pyautogui.write('guest')
    pyautogui.press('tab')
    pyautogui.write('welcome2qauto')
    pyautogui.press('enter')

    time.sleep(1)


def test_registration():
    RegistrationPage.RegistrationPage()

    # time.sleep(10)

