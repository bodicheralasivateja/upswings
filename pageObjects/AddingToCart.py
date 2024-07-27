from selenium.webdriver.common.by import By
import time

from pageObjects.LoginPage import LoginPage


class AddingToCart():
    next_button_xpath = "//button[@id='next2']"
    last_product_xpath = "//a[normalize-space()='MacBook Pro']"
    add_to_cart_xpath = "//a[normalize-space()='Add to cart']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login()
        login_page.username(username)
        login_page.password(password)
        login_page.login_btn()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")

    def clickNext(self):
        next_button = self.driver.find_element(By.XPATH, self.next_button_xpath)
        next_button.click()
        time.sleep(5)

    def selectProduct(self):
        product_link = self.driver.find_element(By.XPATH, self.last_product_xpath)
        product_link.click()
        time.sleep(5)

    def clickAddToCart(self):
        add_to_cart = self.driver.find_element(By.XPATH, self.add_to_cart_xpath)
        add_to_cart.click()
        time.sleep(5)
