import pytest
from chromedriver_py import binary_path
from selenium import webdriver

@pytest.fixture(name="driver", scope="class")
def driver(request):
    driver = webdriver.Chrome(executable_path=binary_path)
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.close()