from selenium.webdriver.common.by import By

class LandingPage:
    url = 'https://littlecaesars.com/en-us/'

    link_logo = (By.XPATH, "(//a[@data-testid = 'header__littleCaesars-logo'])[2]")

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self.url)
        return self

    def link_logo_displayed(self):
        if self._driver.find_element(*self.link_logo).is_displayed():
            return True
