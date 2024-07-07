import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pyautogui


def test_registration():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    url = "https://qauto2.forstudy.space/"
    driver.get(url)

    pyautogui.write('guest')
    pyautogui.press('tab')
    pyautogui.write('welcome2qauto')
    pyautogui.press('enter')

    SIGN_IN_BUTTON = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-outline-white header_signin']")))
    SIGN_IN_BUTTON.click()

    REGISTRATION_BUTTON = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Registration']")))
    REGISTRATION_BUTTON.click()
    time.sleep(1)

    NAME_FIELD = wait.until(EC.element_to_be_clickable((By.ID, "signupName")))
    NAME_FIELD.send_keys("ASAHIK")

    LAST_NAME_FIELD = wait.until(EC.element_to_be_clickable((By.ID, "signupLastName")))
    LAST_NAME_FIELD.send_keys("BIBO")

    EMAIL_FIELD = wait.until(EC.element_to_be_clickable((By.ID, "signupEmail")))
    EMAIL_FIELD.send_keys("ghfgh341gghsdhf@eshdnd.com")

    PASSWORD_FIELD = wait.until(EC.element_to_be_clickable((By.ID, "signupPassword")))
    PASSWORD_FIELD.send_keys("123123Qwe")

    RE_ENTER_PASSWORD_FIELD = wait.until(EC.element_to_be_clickable((By.ID, "signupRepeatPassword")))
    RE_ENTER_PASSWORD_FIELD.send_keys("123123Qwe")

    REGISTER_BUTTON = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-primary']")))
    REGISTER_BUTTON.click()

    time.sleep(3)

    new_url = driver.current_url
    response = requests.get(new_url)
    assert response.status_code == 401, f"Очікую 200, але статус: {response.status_code}"

    GARAGE = wait.until((EC.element_to_be_clickable((By.XPATH, "(//*[text()='Garage'])[1]"))))
    assert "Garage" == GARAGE.text, "Expected text 'Garage', but got something else"

    driver.quit()
