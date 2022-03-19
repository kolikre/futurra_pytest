import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def setup():
    # Set browser options
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1366,768')
    # Set driver
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
