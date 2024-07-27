from selenium.webdriver.common.by import By
import time
from pageObjects.LoginPage import LoginPage

class Logout:
    logout_xpath = "//a[@id='logout2']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login()
        login_page.username(username)
        login_page.password(password)
        login_page.login_btn()
        time.sleep(5)

    def logout(self):
        logout_button = self.driver.find_element(By.XPATH, self.logout_xpath)
        logout_button.click()
        time.sleep(3)
