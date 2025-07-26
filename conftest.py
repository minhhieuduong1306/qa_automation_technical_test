import pytest
from selenium import webdriver
import _globals

@pytest.fixture
def driver():
   # Setup: Initialize the WebDriver
   driver = webdriver.Chrome()
   driver.get(_globals.args.url)
   yield driver
   # Teardown: Quit the WebDriver
   driver.quit()