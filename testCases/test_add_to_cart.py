import time

from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddingToCart import AddingToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestAddToCart:
    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmailAddress()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_add_product_to_cart(self, setup):
        self.logger.info("*** Test_add_product_to_cart ***")
        driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        lp = LoginPage(driver)
        ac = AddingToCart(driver)
        lp.login()
        lp.username(self.username)
        lp.password(self.password)
        lp.login_btn()
        self.logger.info("User logged in successfully")
        time.sleep(2)
        ac.scroll_down()
        ac.clickNext()
        time.sleep(2)
        ac.selectProduct()
        ac.clickAddToCart()
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        self.logger.info("Product added to cart successfully")

