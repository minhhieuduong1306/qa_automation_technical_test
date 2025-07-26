import pytest
from selenium import webdriver
from urllib.parse import urlparse

import _globals # _globals is used to store global variables

def pytest_addoption(parser):
   parser.addoption("--url", action="store", default="https://aqxtrader.aquariux.com", help="URL to test")
   parser.addoption("--userid", action="store", default="998994", help="User ID for login")
   parser.addoption("--password", action="store", default="O6#tod$bpP4$", help="Password for login")

def pytest_configure(config):
   """Configure pytest with global variables."""
   _globals.args = config.option

   # Validate URL format
   url = urlparse(_globals.args.url)
   if not all([url.scheme, url.netloc]):
      raise ValueError(f"Invalid URL: {_globals.args.url}")
   
@pytest.fixture
def driver(request):
   # Setup: Initialize the WebDriver
   driver = webdriver.Chrome()
   driver.get(_globals.args.url)
   yield driver
   # Teardown: Quit the WebDriver
   driver.quit()