from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from time import sleep

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

driver.set_page_load_timeout(5)

try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Successfully accessed the page")
except TimeoutException:
    print("Page load time exceeded the limit.")
finally:
    driver.quit()
