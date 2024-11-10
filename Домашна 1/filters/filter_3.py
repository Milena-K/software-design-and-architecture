from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

from .helpers import insert_from_table_to_db


def fetch_and_update_data(update_codes: dict[str, str]):
    """
    update_codes - dict with codes for keys, value is a date of the last update
    """
    for (issuer_code, fetch_from_date) in update_codes.items():
        fetch_data_for_issuer(issuer_code, fetch_from_date)

def format_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y").strftime("%d.%m.%Y")

def format_price(price):
    return "{:,.2f}".format(price)

def fetch_data_for_issuer(issuer_code, start_date):
    """scrapes table and returns new information about issuer"""
    # select code
    driver = webdriver.Chrome()
    driver.get("https://www.mse.mk/mk/stats/symbolhistory/kmb")
    dropdown = driver.find_element(By.ID, "Code")
    select = Select(dropdown)
    select.select_by_value(issuer_code)
    # enter from date
    fromDate = driver.find_element(By.ID, "FromDate")
    # add a while loop and get data for each year of the past 10 years
    fromDate.send_keys(start_date)
    # click ze button
    button = driver.find_element(By.XPATH, '//*[@value="Прикажи"]')
    button.click()
    insert_from_table_to_db(driver, issuer_code)
