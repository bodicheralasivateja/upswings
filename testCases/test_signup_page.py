import os
import time
import pytest
from pageObjects.SignupPage import SignupPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Signup:
    BaseURL = ReadConfig.getApplicationURL()
    screenshot_dir = r"C:\Users\Lenovo\PycharmProjects\pythonProject\upswings\Screenshots"
    logger = LogGen.loggen()

    # Signup with valid details
    def test_signup_001(self, setup):
        self.logger.info("*** Test_signup_001 ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.sp = SignupPage(self.driver)
        time.sleep(5)
        self.sp.click_signup_button()
        self.sp.enter_username("teja@12322345@gmail.com")
        self.sp.enter_password("Siva@1233")
        time.sleep(2)
        self.sp.click_signup_btn()
        time.sleep(2)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        self.logger.info("*** Sign up successful. ***")

    # Enter a valid username but do not enter a password and attempt to sign up.
    def test_signup_002(self, setup):
        self.logger.info("*** Test_signup_002 ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.sp = SignupPage(self.driver)
        time.sleep(5)
        self.sp.click_signup_button()
        self.sp.enter_username("teja@12322245@gmail.com")
        self.sp.enter_password("")
        time.sleep(2)
        self.sp.click_signup_btn()
        time.sleep(2)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        self.logger.info("*** Please fill out Username and Password***")

    # Do not enter a username or password and attempt to sign up.
    def test_signup_003(self, setup):
        self.logger.info("*** Test_signup_003 ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.sp = SignupPage(self.driver)
        time.sleep(5)
        self.sp.click_signup_button()
        self.sp.enter_username("")
        self.sp.enter_password("")
        time.sleep(2)
        self.sp.click_signup_btn()
        time.sleep(2)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        self.logger.info("*** Please fill out Username and Password. ***")

    # Enter a valid password but do not enter a username and attempt to sign up.
    def test_signup_004(self, setup):
        self.logger.info("*** Test_signup_004 ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.sp = SignupPage(self.driver)
        time.sleep(5)
        self.sp.click_signup_button()
        self.sp.enter_username("")
        self.sp.enter_password("Siva@123")
        time.sleep(2)
        self.sp.click_signup_btn()
        time.sleep(2)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        alert_window.accept()
        self.logger.info("*** Please fill out Username and Password. ***")











