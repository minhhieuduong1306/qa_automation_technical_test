import pytest
from selenium import webdriver

@pytest.fixture
def driver():
   # Setup: Initialize the WebDriver
   driver = webdriver.Chrome()
   yield driver
   # Teardown: Quit the WebDriver
   driver.quit()