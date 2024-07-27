import os
import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmailAddress()
    password = ReadConfig.getPassword()
    screenshot_dir = r"C:\Users\Lenovo\PycharmProjects\pythonProject\upswings\Screenshots"
    logger = LogGen.loggen()

    # Signup with valid details
    def test_signup_001(self, setup):
        self.logger.info("*** Test_signup_001 ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.login()
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.login_btn()
        time.sleep(5)