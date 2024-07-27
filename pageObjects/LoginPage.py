from selenium.webdriver.common.by import By
import time

class LoginPage:
    login_xpath = "//a[@id='login2']"
    username_xpath = "//input[@id='loginusername']"
    password_xpath = "(//input[@id='loginpassword'])[1]"
    login_btn_xpath = "//button[normalize-space()='Log in']"
    logout_xpath = "//a[@id='logout2']"

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        login = self.driver.find_element(By.XPATH, self.login_xpath)
        login.click()
        time.sleep(2)

    def username(self, username):
        username_field = self.driver.find_element(By.XPATH, self.username_xpath)
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)

    def password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.password_xpath)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

    def login_btn(self):
        login_button = self.driver.find_element(By.XPATH, self.login_btn_xpath)
        login_button.click()
        time.sleep(2)

    def logout(self):
        logout_link = self.driver.find_element(By.XPATH, self.logout_xpath)
        logout_link.click()






