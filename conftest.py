import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")

def browser():
    # Configuração do webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/home/mmelo/chrome-linux64/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()