from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
