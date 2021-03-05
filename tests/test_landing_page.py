import pytest
from pages import LandingPage


@pytest.fixture(name="setup")
def setup(driver):
    global landing_page
    landing_page = LandingPage(driver)
    landing_page.open()

@pytest.mark.usefixtures('driver')
class TestLandingPage:
    def test_link_logo_displayed(self, setup):
        assert landing_page.link_logo_displayed()

    def test_div_start_online_order_displayed(self):
        assert landing_page.div_start_online_order_displayed()




