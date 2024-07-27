import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from pageObjects.LoginPage import LoginPage


class Checkout:
    cart_xpath = "//a[normalize-space()='Cart']"
    cart_items_xpath = "//td[normalize-space()='MacBook Pro']"
    place_order_button_xpath = "//button[normalize-space()='Place Order']"
    total_price_xpath = "//h3[@id='totalp']"
    delete_item_xpath = "//a[normalize-space()='Delete']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login()
        login_page.username(username)
        login_page.password(password)
        login_page.login_btn()

    def cart(self):
        cart_button = self.driver.find_element(By.XPATH, self.cart_xpath)
        cart_button.click()
        time.sleep(5)

    def getCartItems(self):
        return self.driver.find_elements(By.XPATH, self.cart_items_xpath)

    def getTotalPrice(self):
        total_price_element = self.driver.find_element(By.XPATH, self.total_price_xpath)
        return total_price_element.text

    def clickPlaceOrder(self):
        place_order_button = self.driver.find_element(By.XPATH, self.place_order_button_xpath)
        place_order_button.click()
        time.sleep(5)

    def deleteItems(self):

        try:

            elements = self.driver.find_element(By.XPATH, "//tbody[@id='tbodyid']/child::tr")

            for element in elements:
                if element.is_displayed():
                    delete_button = element.find_element(By.XPATH, self.delete_item_xpath)
                    delete_button.click()
                    wait.until(EC.invisibility_of_element(element))

        except NoSuchElementException as e:
            print(f"An element was not found: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")




