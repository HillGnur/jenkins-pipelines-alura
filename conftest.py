import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")

def browser():
    # Configuração do webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    service=Service(executable_path="/home/mmelo/chrome-linux64/chrome")
    driver=webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()