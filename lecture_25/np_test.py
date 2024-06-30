import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://tracking.novaposhta.ua/#/uk')

wait = WebDriverWait(driver, 10)

def test_tracking():
    try:
        tracking_button = wait.until(EC.element_to_be_clickable((By.ID, "en")))
        tracking_button.send_keys("20450941657619")

        find_button = wait.until(EC.element_to_be_clickable((By.ID, "en")))
        find_button = wait.until(EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en")))
        find_button.click()

        good_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[5]")))
        good_button.click()

        status_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header__status-text']")))

        assert status_message.text == 'Отримана', f"Очікуємий статус: 'Отримана', але актуальний статус: '{status_message.text}'"
        print("Посилка отримана")

        time.sleep(1)

    finally:
        driver.quit()
