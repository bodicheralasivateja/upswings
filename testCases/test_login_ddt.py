import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis


class Test_002_DDT_Login:
    BaseURL = ReadConfig.getApplicationURL()
    path = 'C:\\Users\\Lenovo\\PycharmProjects\\pythonProject\\upswings\\TestData\\LoginData.xlsx'
    screenshot_dir = r"C:\Users\Lenovo\PycharmProjects\pythonProject\upswings\Screenshots"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("Test_002_DDT_login")
        self.logger.info("*** Test_login ***")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.rows = XLUtilis.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilis.readData(self.path, 'Sheet1', r, 2)
            self.status = XLUtilis.readData(self.path, 'Sheet1', r, 3)
            if r==2 or r==3:
                self.lp.login()
            else:pass

            self.lp.username(self.user)
            self.lp.password(self.password)
            self.lp.login_btn()


            try:
                alert = self.driver.switch_to.alert
                print(alert.text)
                alert.accept()
            except NoAlertPresentException:
                self.logger.warning("No alert present after login.")

            time.sleep(2)

            act_title = self.driver.title
            exp_title = "STORE"

            if act_title == exp_title:
                if self.status == "Pass":
                    self.logger.info("***** Passed *****")
                    time.sleep(3)
                    self.lp.logout()
                    time.sleep(2)
                    lst_status.append("Pass")
                elif self.status == "Fail":
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
            else:
                if self.status == "Pass":
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
                elif self.status == "Fail":
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT test passed. *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test failed. *****")
            self.driver.close()

