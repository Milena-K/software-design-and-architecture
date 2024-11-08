from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sqlite3

from helpers import insert_from_table_to_db

def check_last_data(issuer_codes):
    conn = sqlite3.connect('stock_issuers.db')
    cursor = conn.cursor()
    fetch_data_info = {}
    for code in issuer_codes:
        cursor.execute("SELECT MAX(date) FROM IssuerData WHERE code = ?", (code,))
        last_date = cursor.fetchone()[0]

        if last_date:
            last_date = datetime.strptime(last_date, "%d.%m.%Y").date()
            fetch_data_info[code] = {
                "fetch_from_date": last_date + timedelta(days=1)
            }
        else:
            load_10y_information(code)

    conn.close()

    print(fetch_data_info)
    return fetch_data_info


driver = webdriver.Chrome()
driver.get("https://www.mse.mk/mk/stats/symbolhistory/kmb")

def load_10y_information(issuer_code):
    # select code
    dropdown = driver.find_element(By.ID, "Code")
    select = Select(dropdown)
    select.select_by_value(issuer_code)
    # enter from date
    fromDate = driver.find_element(By.ID, "FromDate")
    # add a while loop and get data for each year of the past 10 years
    this_year = datetime.now()
    year = 0
    while year < 10:
        year += 1
        last_year = (this_year - timedelta(days=364))
        last_year_str = last_year.date().strftime("%d.%m.%Y")
        fromDate.send_keys(last_year_str)
        this_year = last_year
        # click ze button
        button = driver.find_element(By.XPATH, '//*[@value="Прикажи"]')
        button.click()
        insert_from_table_to_db()
