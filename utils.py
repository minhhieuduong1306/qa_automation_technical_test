from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):
   """Base class for pages."""
   def __init__(self, driver):
      self.driver = driver

   def wait_for_xpath_clickable(self, xpath, timeout=30):
      return WebDriverWait(self.driver, timeout).until(
         EC.element_to_be_clickable((By.XPATH, xpath))
      )

   def wait_for_xpath_visible(self, xpath, timeout=30):
      return WebDriverWait(self.driver, timeout).until(
         EC.visibility_of_element_located((By.XPATH, xpath))
      )