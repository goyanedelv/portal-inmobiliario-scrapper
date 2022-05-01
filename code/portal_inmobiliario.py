from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time
import datetime

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options = options, executable_path = "C:/Users/goyan/Documents/Software/chromedriver_win32/101/chromedriver.exe")

with open("data/seed/portal_inmobiliario_seed_4.txt") as f:
        lines = f.readlines()


for line in lines:
    ct = datetime.datetime.now()
    time_tag = str(ct).replace(":","").replace(" ","-")[:17]

    all_info = []

    driver.get(line.replace("\n",""))

    time.sleep(3)

    precio = driver.find_elements(By.XPATH, "//span[contains(@class, 'price-tag-text-sr-only')]")
    time.sleep(3)

    metraje = driver.find_elements(By.XPATH, "//li[contains(@class, 'ui-search-card-attributes__attribute')]")
    time.sleep(3)

    location = driver.find_elements(By.XPATH, "//p[contains(@class, 'ui-search-item__group__element ui-search-item__location')]")

    for elem in precio:
        all_info.append(elem.text)

    for elem in metraje:
        all_info.append(elem.text)

    for elem in location:
        all_info.append(elem.text)

    with open(f"data/raw_output/port_inmob_{time_tag}_raw.txt", "w", encoding="utf-8") as f:
        for line in all_info:
            _ = f.write(line)
            _ = f.write('\n')