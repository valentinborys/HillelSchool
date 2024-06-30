import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://localhost:8000/dz.html")

driver.switch_to.frame("frame1")

input1 = driver.find_element(By.ID, "input1")
input1.send_keys("Frame1_Secret")
time.sleep(1)

verify_button1 = driver.find_element(By.XPATH, "//button[contains(text(),'Перевірити')]")
verify_button1.click()
time.sleep(1)

alert1 = WebDriverWait(driver, 10).until(EC.alert_is_present())
assert "Верифікація пройшла успішно!" in alert1.text
alert1.accept()
time.sleep(1)

driver.switch_to.default_content()
driver.switch_to.frame("frame2")
time.sleep(1)

input2 = driver.find_element(By.ID, "input2")
input2.send_keys("Frame2_Secret")

verify_button2 = driver.find_element(By.XPATH, "//button[contains(text(),'Перевірити')]")
verify_button2.click()
time.sleep(1)

alert2 = WebDriverWait(driver, 10).until(EC.alert_is_present())
assert "Верифікація пройшла успішно!" in alert2.text
alert2.accept()

time.sleep(10)
