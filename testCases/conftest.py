import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("Launching Chrome browser")
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("Launching Firefox browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name: chrome or firefox")


def pytest_configure(config):
    config._metadata = {
        'Base URL': 'https://www.demoblaze.com/',
        'Project Name': ' PRODUCT STORE',
    }