from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time


class HomePage:
    PRODUCT_CARDS_XPATH = "//div[@class='card h-100']"
    PRODUCT_NAMES_XPATH = "//div[@class='card h-100']//a[@class='hrefch']"
    PRODUCT_PRICES_XPATH = "//div[@class='card h-100']//h5"

    def __init__(self, driver):
        self.driver = driver

    def get_product_elements(self):
        return self.driver.find_elements(By.XPATH, self.PRODUCT_CARDS_XPATH)

    def get_product_names(self):
        return self.driver.find_elements(By.XPATH, self.PRODUCT_NAMES_XPATH)

    def get_product_prices(self):
        return self.driver.find_elements(By.XPATH, self.PRODUCT_PRICES_XPATH)


class CategoryPage:
    CATEGORY_LINKS_XPATH = "//a[@id='cat']"
    PRODUCT_TITLE_XPATH = "//a[normalize-space()='Samsung galaxy s6']"

    def __init__(self, driver):
        self.driver = driver

    def get_category_links(self):
        retries = 3
        for _ in range(retries):
            try:
                return self.driver.find_elements(By.XPATH, self.CATEGORY_LINKS_XPATH)
            except StaleElementReferenceException:
                if _ < retries - 1:
                    continue
                else:
                    raise

    def get_product_titles(self):
        return self.driver.find_elements(By.XPATH, self.PRODUCT_TITLE_XPATH)




