from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ProductBrowsing import HomePage
from pageObjects.ProductBrowsing import CategoryPage
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig


class TestHomePage:
    BaseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmailAddress()
    password = ReadConfig.getPassword()
    screenshot_dir = r"C:\Users\Lenovo\PycharmProjects\pythonProject\upswings\Screenshots"
    logger = LogGen.loggen()

    def test_products_displayed(self, setup):
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.login()
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.login_btn()
        time.sleep(5)
        self.logger.info("**** Test: Products Displayed on Homepage ****")

        home_page = HomePage(setup)
        time.sleep(3)
        product_elements = home_page.get_product_elements()
        product_names = home_page.get_product_names()
        product_prices = home_page.get_product_prices()

        assert len(product_elements) > 0, "No products found on the homepage."
        assert len(product_names) == len(product_prices), "Mismatch in number of product names and prices."
        for name, price in zip(product_names, product_prices):
            self.logger.info(f"Product Name: {name.text}, Price: {price.text}")

    def test_navigate_product_categories(self, setup):
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.login()
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.login_btn()
        category_page = CategoryPage(self.driver)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, category_page.CATEGORY_LINKS_XPATH))
        )

        self.logger.info("**** Test: Products Displayed on Homepage ****")
        categories = category_page.get_category_links()
        assert len(categories) > 0, "No categories found on the homepage."

        for category in categories:
            category_name = category.text
            category.click()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, category_page.PRODUCT_TITLE_XPATH))
            )
            product_titles = category_page.get_product_titles()
            assert len(product_titles) > 0, f"No products found for category {category_name}"

            self.logger.info(f"Category: {category_name}")
            for product in product_titles:
                self.logger.info(f"Product: {product.text}")

            self.driver.get(self.BaseURL)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, category_page.CATEGORY_LINKS_XPATH))
            )
