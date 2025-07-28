import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
   """Base class for pages."""
   def __init__(self, driver):
      self.driver = driver

   def wait_for_xpath_clickable(self, xpath, timeout=30):
      WebDriverWait(self.driver, timeout).until(
         EC.element_to_be_clickable((By.XPATH, xpath))
      )
      # Scroll to the element to ensure it's in view
      e = self.driver.find_element(By.XPATH, xpath)
      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", e)
      ActionChains(self.driver).move_to_element(e).pause(0.3).perform() # Ensure the element is fully rendered
      return e

   def wait_for_xpath_visible(self, xpath, timeout=30):
      WebDriverWait(self.driver, timeout).until(
         EC.visibility_of_element_located((By.XPATH, xpath))
      )
      # Scroll to the element to ensure it's in view
      e = self.driver.find_element(By.XPATH, xpath)
      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", e)
      time.sleep(0.3) # Ensure the element is fully rendered
      return e
