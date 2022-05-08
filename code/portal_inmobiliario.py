from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import datetime
import yaml

with open("parametros.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options = options, executable_path = parameters['chromedriver'])

with open(f"data/seed/{sys.argv[1]}") as f:
        lines = f.readlines()

lines_length = len(lines)
progress_counter = 0
for line in lines:
    ct = datetime.datetime.now()
    time_tag = str(ct).replace(":","").replace(" ","-")[:17]

    all_info = []

    driver.get(line.replace("\n",""))

    time.sleep(3)

    all = driver.find_elements(By.XPATH, "//a[contains(@class, 'ui-search-result__content-wrapper ui-search-link')]")

    for elem in all:
        all_info.append(elem.text)

    with open(f"data/raw_output/00_port_inmob_{time_tag}_raw.txt", "w", encoding="utf-8") as f:
        for line in all_info:
            _ = f.write(line)
            _ = f.write('\n')
    progress_counter += 1

    sys.stdout.write(f"\rProgreso: {progress_counter} de {lines_length}")
    sys.stdout.flush()