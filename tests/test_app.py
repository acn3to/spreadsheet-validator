import pytest
import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.set_page_load_timeout(5)
    yield driver

    driver.quit()
    process.kill()


def test_app_opens(driver):
    driver.get("http://localhost:8501")
    sleep(5)
