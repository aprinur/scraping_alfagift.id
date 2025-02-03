import os
import time
import pandas
import datetime
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def press_button(tag: str):
    try:
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tag)))
        driver.execute_script("arguments[0].click();", next_button)
        return True
    except Exception as e:
        print(f'Error pressing button: {e}')
        return False


def get_html(url):
    driver.get(url)
    time.sleep(2)
    return driver.page_source


def get_current_url():
    return driver.page_source


def save_to_file(product, filename):
    save_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    date = datetime.datetime.now().strftime('%d_%B_%Y')
    excel_path = os.path.join(save_dir, f'{filename}_{date}.xlsx')
    csv_path = os.path.join(save_dir, f'{filename}_{date}.csv')
    df = pandas.DataFrame(product)

    df.to_excel(excel_path, index=False, engine='openpyxl')
    df.to_csv(csv_path, index=False)


def wait_emergence(class_name):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, f"{class_name}")))

