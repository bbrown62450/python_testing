import pytest
from chromedriver_py import binary_path
from selenium import webdriver

driver = webdriver.Chrome(executable_path=binary_path)
driver.implicitly_wait(5)