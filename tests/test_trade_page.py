import pytest
from pages_locators.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestTradePage():
   """Test class for trade page."""
   @pytest.fixture(autouse=True)
   def setup_page(self, driver):
      self.driver = driver
      self.login_page = LoginPage(self.driver)

   def test_place_order_by_price(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("Top Gainer")
      trade_page.select_market("XAUUSD")
      trade_page.select_order_type("Market")
      trade_page.volume = 10
      trade_page.stop_loss_price = 3333.5
      trade_page.take_profit_price = 3340.5
      # trade_page.place_order() # Disabled due to "Market Closed" or "Stay Tuned" status

   def test_place_order_by_points(self):
      trade_page = self.login_page.navigate_to_trade()
      trade_page.filter_markets("Top Gainer")
      trade_page.select_market("XAGUSD")
      trade_page.select_order_type("Market")
      trade_page.volume = 10
      trade_page.stop_loss_points = 350
      trade_page.take_profit_points = 350