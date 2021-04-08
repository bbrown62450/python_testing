import pytest
from chromedriver_py import binary_path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name="driver", scope="class")
def driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.close()