import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Checkout import Checkout
from pageObjects.AddingToCart import AddingToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestAddToCart:
    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmailAddress()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_checkout_successfully(self, setup):
        self.logger.info("*** Starting Test: Successfully Add to Cart ***")
        driver = setup
        self.driver = driver
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        ck = Checkout(self.driver)
        ac = AddingToCart(self.driver)
        lp.login()
        lp.username(self.username)
        lp.password(self.password)
        lp.login_btn()

        self.logger.info("Login successful")
        time.sleep(2)
        ac.scroll_down()
        ac.clickNext()
        time.sleep(2)
        ac.selectProduct()
        ac.clickAddToCart()
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        ck.cart()
        time.sleep(4)
        ck.getCartItems()
        ck.getTotalPrice()
        ck.clickPlaceOrder()
        self.logger.info("Checkout process initiated")

    def test_checkout(self, setup):
        self.logger.info("*** Starting Test: Checkout without Adding Items ***")
        driver = setup
        self.driver = driver
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        ck = Checkout(self.driver)
        lp.login()
        lp.username(self.username)
        lp.password(self.password)
        lp.login_btn()
        self.logger.info("Login successful")
        ck.cart()
        ck.deleteItems()
        time.sleep(2)
        ck.clickPlaceOrder()
        self.logger.info("Checked out with no items. Cart is empty.")
