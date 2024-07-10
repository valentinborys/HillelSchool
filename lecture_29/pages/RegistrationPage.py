from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lecture_29.pages.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver=None):
        if driver is None:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def open_browser(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def current_sites_url(self):
        return self.driver.current_url
