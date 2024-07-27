from selenium.webdriver.common.by import By
import time


class SignupPage:
    signup_button_xpath = "//a[@id='signin2']"
    username_xpath = '//input[@id="sign-username"]'
    password_xpath = '//input[@id="sign-password"]'
    signup_btn_xpath = "//button[contains(text(),'Sign up')]"

    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_btn = self.driver.find_element(By.XPATH, self.signup_button_xpath)
        signup_btn.click()
        time.sleep(2)

    def enter_username(self, username):
        username_field = self.driver.find_element(By.XPATH, self.username_xpath)
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.password_xpath)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(5)

    def click_signup_btn(self):
        signup_btn = self.driver.find_element(By.XPATH, self.signup_btn_xpath)
        signup_btn.click()
        time.sleep(5)
