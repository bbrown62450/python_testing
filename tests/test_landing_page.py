import pytest
from pages import LandingPage
from conftest import driver

@pytest.fixture(name="setup")
def setup():
    global landing_page
    landing_page = LandingPage(driver)
    landing_page.open()

def test_link_logo_displayed(setup):
    assert landing_page.link_logo_displayed()

def teardown():
    driver.close()




