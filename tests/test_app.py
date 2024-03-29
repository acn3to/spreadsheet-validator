import pytest
import subprocess
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


def test_check_title_is(driver):
    driver.get("http://localhost:8501")
    sleep(5)

    page_title = driver.title

    expected_title = "Excel Schema Validator"
    assert page_title == expected_title, f"The page title was '{page_title}', but expected '{expected_title}'"


def test_check_streamlit_h1(driver):
    driver.get("http://localhost:8501")
    sleep(5)

    h1_element = driver.find_element(By.TAG_NAME, "h1")

    expected_text = "Insert your spreadsheet for validation"
    assert h1_element.text == expected_text


def test_check_user_can_upload_an_excel_and_receive_a_message(driver):
    driver.get("http://localhost:8501")

    sleep(5)

    success_file_path = os.path.abspath("data/spreadsheet.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    sleep(5)
    assert "The Excel file schema is correct!" in driver.page_source


def test_failed_upload(driver):
    driver.get("http://localhost:8501")

    sleep(5)

    failure_file_path = os.path.abspath("data/failure.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(failure_file_path)

    sleep(5)
    assert "Validation error" in driver.page_source
