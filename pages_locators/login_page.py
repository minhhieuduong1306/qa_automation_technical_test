from utils import Page
import _globals  # _globals is used to store global variables

class LoginPage(Page):
   """Class for login page."""
   def __init__(self, driver):
      self.driver = driver
      self.login(userid=_globals.args.userid,
                 password=_globals.args.password)

   userid_input_xpath = "//input[@data-testid='login-user-id']"
   password_input_xpath = "//input[@data-testid='login-password']"
   sign_in_button_xpath = "//button[@data-testid='login-submit']"
   trade_option_xpath = "//*[@data-testid='side-bar-option-trade']"

   def login(self, userid, password):
      """Method to perform login action."""
      self.wait_for_xpath_visible(self.userid_input_xpath).send_keys(userid)
      self.wait_for_xpath_visible(self.password_input_xpath).send_keys(password)
      self.wait_for_xpath_visible(self.sign_in_button_xpath).click()
      self.wait_for_xpath_visible(self.trade_option_xpath)