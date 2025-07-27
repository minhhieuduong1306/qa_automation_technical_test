import pytest
from pages_locators.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestTradePage():
   """Test class for trade page."""
   @pytest.fixture(autouse=True)
   def setup_page(self, driver):
      self.driver = driver
      self.login_page = LoginPage(self.driver)

   def test_place_market_buy_order_by_price(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("GBPAUD")
      trade_page.select_order_type("Market")
      trade_page.volume = 1
      trade_page.stop_loss_price = 2.0
      trade_page.take_profit_price = 2.1
      trade_page.place_buy_order()
      trade_page.confirm_order()
      trade_page.verify_order_notification_message('Market Order Submitted')

   def test_place_market_buy_order_by_points(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDCAD")
      trade_page.select_order_type("Market")
      trade_page.volume = 10
      trade_page.stop_loss_points = 1000
      trade_page.take_profit_points = 1000
      trade_page.place_buy_order()
      trade_page.confirm_order()
      trade_page.verify_order_notification_message('Market Order Submitted')

   def test_edit_open_position(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDCAD")
      trade_page.open_positions()
      trade_page.edit_open_positions(1) # The first open position in the list
      trade_page.edit_stop_loss_points = 500
      trade_page.edit_take_profit_points = 500
      trade_page.update_buy_order()
      trade_page.confirm_update_order()
      trade_page.verify_order_notification_message('Market Order Updated')
   
   def test_partial_close_open_position(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDCAD")
      trade_page.open_positions()
      trade_page.close_open_positions(1) # The first open position in the list
      trade_page.close_order_volume = 5
      trade_page.close_order()
      trade_page.verify_order_notification_message('Close Order')

   def test_close_open_position(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDCAD")
      trade_page.open_positions()
      trade_page.close_open_positions(1) # The first open position in the list
      trade_page.close_order()
      trade_page.verify_order_notification_message('Close Order')

   @pytest.mark.parametrize("expiry", ["Good Till Cancelled", "Good Till Day",
                                       "Specified Date", "Specified Date and Time"])
   def test_place_limit_buy_order_with_expiry(self, expiry):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDJPY")
      trade_page.select_order_type("Limit")
      trade_page.volume = 10
      trade_page.price = 95
      trade_page.stop_loss_points = 500
      trade_page.take_profit_points = 2500
      trade_page.select_expiry(expiry)
      if expiry == "Specified Date":
         trade_page.set_expiry_date("July 31")
      elif expiry == "Specified Date and Time":
         trade_page.set_expiry_date("July 31")
         trade_page.set_expiry_time("03:00")
      trade_page.place_buy_order()
      trade_page.confirm_order()
      trade_page.verify_order_notification_message('Limit Order Submitted')

   @pytest.mark.parametrize("expiry", ["Good Till Cancelled", "Good Till Day",
                                       "Specified Date", "Specified Date and Time"])
   def test_place_stop_buy_order_with_expiry(self, expiry):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("All")
      trade_page.select_market("AUDJPY")
      trade_page.select_order_type("Stop")
      trade_page.volume = 10
      trade_page.price = 98
      trade_page.stop_loss_points = 1500
      trade_page.take_profit_points = 1000
      trade_page.select_expiry(expiry)
      if expiry == "Specified Date":
         trade_page.set_expiry_date("July 31")
      elif expiry == "Specified Date and Time":
         trade_page.set_expiry_date("July 31")
         trade_page.set_expiry_time("03:00")
      trade_page.place_buy_order()
      trade_page.confirm_order()
      trade_page.verify_order_notification_message('Stop Order Submitted')