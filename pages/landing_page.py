from selenium.webdriver.common.by import By
from src.testproject.sdk.drivers import webdriver


class LandingPage:
    url = 'https://littlecaesars.com/en-us/'

    link_logo = (By.XPATH, "(//a[@data-testid = 'header__littleCaesars-logo'])[2]")
    div_start_online_order = (By.XPATH, "//div[contains(text(), 'Start Online Order')]")

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self.url)
        return self

    def link_logo_displayed(self):
        if self._driver.find_element(*self.link_logo).is_displayed():
            return True

    def div_start_online_order_displayed(self):
        if self._driver.find_element(*self.div_start_online_order).is_displayed():
            return True
