import selenium.webdriver.common.by as By

class LoginPage(object):
   """Class for login page."""
   def __init__(self, driver, username, password):
      self.driver = driver
      self.login(username, password)

   userid_input_xpath = (By.XPATH, "//input[@data-testid='login-user-id']")
   password_input_xpath = (By.XPATH, "//input[@data-testid='login-password']")
   sign_in_button_xpath = (By.XPATH, "//button[@data-testid='login-submit']")

   def login(self, username, password):
      """Method to perform login action."""
      self.driver.find_element(*self.userid_input_xpath).send_keys(username)
      self.driver.find_element(*self.password_input_xpath).send_keys(password)
      self.driver.find_element(*self.sign_in_button_xpath).click()