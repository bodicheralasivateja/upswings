import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Logout import Logout
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestAddToCart:
    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmailAddress()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_checkout_successfully(self, setup):
        self.logger.info("*** Successfully added ***")
        driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        lp = LoginPage(driver)
        lg = Logout(driver)
        lp.login()
        lp.username(self.username)
        lp.password(self.password)
        lp.login_btn()
        time.sleep(5)
        lg.logout()
