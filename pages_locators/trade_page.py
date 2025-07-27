from utils import Page
from selenium.webdriver.common.keys import Keys

class TradePage(Page):
   """Class for trade page."""
   def __init__(self, driver):
      self.driver = driver

   # Locators for trade page elements
   # Place Buy order
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
   confirm_order_button_xpath = "//button[@data-testid='trade-confirmation-button-confirm']"
   oder_notification_message_xpath = "//*[@data-testid='notification-title' and normalize-space()='{0}']"

   # Open positions
   open_positions_xpath = "//*[@data-testid='tab-asset-order-type-open-positions']"
   edit_open_positions_xpath = "//tbody[@data-testid='asset-open-list']/tr[{}]//*[@data-testid='asset-open-button-edit']"
   edit_stop_loss_points_input_xpath = "//input[@data-testid='edit-input-stoploss-points']"
   edit_take_profit_points_input_xpath = "//input[@data-testid='edit-input-takeprofit-points']"
   update_buy_order_button_xpath = "//button[@data-testid='edit-button-order']"
   confirm_update_order_button_xpath = "//button[@data-testid='edit-confirmation-button-confirm']"
   close_open_positions_xpath = "//tbody[@data-testid='asset-open-list']/tr[{}]//*[@data-testid='asset-open-button-close']"
   close_order_volume_input_xpath = "//input[@data-testid='close-order-input-volume']"
   close_order_button_xpath = "//button[@data-testid='close-order-button-submit']"

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

   def place_buy_order(self):
      """Method to place order"""
      self.wait_for_xpath_clickable(self.trade_order_button_xpath).click()

   def confirm_order(self):
      """Method to confirm order"""
      self.wait_for_xpath_clickable(self.confirm_order_button_xpath).click()

   def verify_order_notification_message(self, message):
      """Method to verify order submission"""
      return self.wait_for_xpath_visible(self.oder_notification_message_xpath.format(message)).is_displayed()

   def open_positions(self):
      """Method to chose open positions"""
      self.wait_for_xpath_clickable(self.open_positions_xpath).click()

   def edit_open_positions(self, row):
      """Method to click edit open positions based on the row number"""
      self.wait_for_xpath_clickable(self.edit_open_positions_xpath.format(row)).click()

   def close_open_positions(self, row):
      """Method to click close open positions based on the row number"""
      self.wait_for_xpath_clickable(self.close_open_positions_xpath.format(row)).click()

   @property
   def edit_stop_loss_points(self):
      return self.wait_for_xpath_visible(self.edit_stop_loss_points_input_xpath).get_attribute('value')

   @edit_stop_loss_points.setter
   def edit_stop_loss_points(self, points):
      if self.edit_stop_loss_points != str(points):
         e = self.wait_for_xpath_visible(self.edit_stop_loss_points_input_xpath)
         e.send_keys(Keys.CONTROL + 'a')  # Select all text
         e.send_keys(points)
         e.send_keys(Keys.TAB)

   @property
   def edit_take_profit_points(self):
      return self.wait_for_xpath_visible(self.edit_take_profit_points_input_xpath).get_attribute('value')

   @edit_take_profit_points.setter
   def edit_take_profit_points(self, points):
      if self.edit_take_profit_points != str(points):
         e = self.wait_for_xpath_visible(self.edit_take_profit_points_input_xpath)
         e.send_keys(Keys.CONTROL + 'a')  # Select all text
         e.send_keys(points)
         e.send_keys(Keys.TAB)

   def update_buy_order(self):
      """Method to update buy order"""
      self.wait_for_xpath_clickable(self.update_buy_order_button_xpath).click()

   def confirm_update_order(self):
      """Method to confirm update order"""
      self.wait_for_xpath_clickable(self.confirm_update_order_button_xpath).click()

   @property
   def close_order_volume(self):
      return self.wait_for_xpath_visible(self.close_order_volume_input_xpath).get_attribute('value')

   @close_order_volume.setter
   def close_order_volume(self, points):
      if self.close_order_volume != str(points):
         e = self.wait_for_xpath_visible(self.close_order_volume_input_xpath)
         e.send_keys(Keys.CONTROL + 'a')  # Select all text
         e.send_keys(points)
         e.send_keys(Keys.TAB)

   def close_order(self):
      """Method to close order"""
      self.wait_for_xpath_clickable(self.close_order_button_xpath).click()
