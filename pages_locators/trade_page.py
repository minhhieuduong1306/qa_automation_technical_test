from utils import Page
from selenium.webdriver.common.keys import Keys

class TradePage(Page):
   """Class for trade page."""
   def __init__(self, driver):
      self.driver = driver

   # Locators for trade page elements
   markets_filter_xpath = "//*[contains(@data-testid, 'tab') and normalize-space()='{0}']"
   market_name_xpath = "//*[normalize-space()='{0}']/ancestor::*[@data-testid='watchlist-list-item']"
   order_type_dropdown_xpath = "//*[@data-testid='trade-dropdown-order-type']"
   order_type_dropdown_value_xpath = "//*[normalize-space()='{0}']"
   volume_input_xpath = "//input[@data-testid='trade-input-volume']"
   stop_loss_price_input_xpath = "//input[@data-testid='trade-input-stoploss-price']"
   stop_loss_points_input_xpath = "//input[@data-testid='trade-input-stoploss-points']"
   take_profit_price_input_xpath = "//input[@data-testid='trade-input-takeprofit-price']"
   take_profit_points_input_xpath = "//input[@data-testid='trade-input-takeprofit-points']"
   trade_order_button_xpath = "//button[@data-testid='trade-button-order']"

   def filter_markets(self, market_name):
      """Method to filter markets"""
      self.wait_for_xpath_clickable(self.markets_filter_xpath.format(market_name)).click()

   def select_market(self, market_name):
      """Method to select market"""
      self.wait_for_xpath_clickable(self.market_name_xpath.format(market_name)).click()

   def select_order_type(self, order_type):
      """Method to select order type"""
      self.wait_for_xpath_clickable(self.order_type_dropdown_xpath).click()
      self.wait_for_xpath_clickable(self.order_type_dropdown_value_xpath.format(order_type)).click()

   @property
   def volume(self):
      return self.wait_for_xpath_visible(self.volume_input_xpath).get_attribute('value')
   
   @volume.setter
   def volume(self, value):
      if self.volume != str(value):
         e = self.wait_for_xpath_visible(self.volume_input_xpath)
         e.clear()
         e.send_keys(value)
         e.send_keys(Keys.TAB)

   @property
   def stop_loss_price(self):
      return self.wait_for_xpath_visible(self.stop_loss_price_input_xpath).get_attribute('value')

   @stop_loss_price.setter
   def stop_loss_price(self, price):
      if self.stop_loss_price != str(price):
         e = self.wait_for_xpath_visible(self.stop_loss_price_input_xpath)
         e.clear()
         e.send_keys(price)
         e.send_keys(Keys.TAB)

   @property
   def stop_loss_points(self):
      return self.wait_for_xpath_visible(self.stop_loss_points_input_xpath).get_attribute('value')

   @stop_loss_points.setter
   def stop_loss_points(self, points):
      if self.stop_loss_points != str(points):
         e = self.wait_for_xpath_visible(self.stop_loss_points_input_xpath)
         e.clear()
         e.send_keys(points)
         e.send_keys(Keys.TAB)

   @property
   def take_profit_price(self):
      return self.wait_for_xpath_visible(self.take_profit_price_input_xpath).get_attribute('value')

   @take_profit_price.setter
   def take_profit_price(self, price):
      if self.take_profit_price != str(price):
         e = self.wait_for_xpath_visible(self.take_profit_price_input_xpath)
         e.clear()
         e.send_keys(price)
         e.send_keys(Keys.TAB)

   @property
   def take_profit_points(self):
      return self.wait_for_xpath_visible(self.take_profit_points_input_xpath).get_attribute('value')

   @take_profit_points.setter
   def take_profit_points(self, points):
      if self.take_profit_points != str(points):
         e = self.wait_for_xpath_visible(self.take_profit_points_input_xpath)
         e.clear()
         e.send_keys(points)
         e.send_keys(Keys.TAB)

   def place_order(self):
      """Method to place order"""
      self.wait_for_xpath_clickable(self.trade_order_button_xpath).click()
