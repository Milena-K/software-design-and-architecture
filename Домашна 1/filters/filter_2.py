from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sqlite3

from .helpers import insert_from_table_to_db

def check_last_data(issuer_codes):
    conn = sqlite3.connect("scraped_data.db")
    cursor = conn.cursor()
    fetch_data_info = {}
    for code in issuer_codes:
        try:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS data_table_{code} (
                    Transaction_Date DATE,
                    Price_Of_Last_Transaction REAL,
                    Max REAL,
                    Min REAL,
                    Average_Price REAL,
                    Percent_Change REAL,
                    Quantity INTEGER,
                    Turnover_BEST_denars INTEGER,
                    Total_Turnover_denars INTEGER
                )
            """)
            cursor.execute(f"SELECT MAX(Transaction_Date) FROM data_table_{code}")
            last_date = cursor.fetchone()[0]
            if last_date:
                last_date = datetime.strptime(last_date, "%d.%m.%Y").date()
                fetch_data_info[code] = {
                    "fetch_from_date": last_date + timedelta(days=1)
                }
            else:
                load_10y_information(code)
        except sqlite3.OperationalError as e:
            print("OperationalError:", e)

    conn.close()
    print(fetch_data_info)
    return fetch_data_info


driver = webdriver.Chrome()
driver.get("https://www.mse.mk/mk/stats/symbolhistory/kmb")

def load_10y_information(issuer_code):
    # add a while loop and get data for each year of the past 10 years
    this_year = datetime.now()
    year = 0
    ####### TODO: add a waiting timer / check if every element is loaded
    while year < 10:
        previous_year = (this_year - timedelta(days=365))
        previous_year_str = previous_year.date().strftime("%d.%m.%Y")
        print("previous_year_str")
        print(previous_year_str)
        # select issuer code
        dropdown = driver.find_element(By.ID, "Code")
        select = Select(dropdown)
        select.select_by_value(issuer_code)
        # enter from date
        fromDate = driver.find_element(By.ID, "FromDate")
        fromDate.clear()
        fromDate.send_keys(previous_year_str)
        # enter to Date
        toDate = driver.find_element(By.ID, "ToDate")
        this_year_str = this_year.date().strftime("%d.%m.%Y")
        print("this_year_str")
        print(this_year_str)
        toDate.clear()
        toDate.send_keys(this_year_str)
        # click ze button
        button = driver.find_element(By.XPATH, '//*[@value="Прикажи"]')
        button.click()
        # Wait up to 10 seconds for the table to be present
        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )
        except TimeoutException as ex:
            print("Table not found or page took too long to load.")
            # prepare for next loop
            this_year = previous_year
            year += 1

        insert_from_table_to_db(driver, issuer_code)
        # prepare for next loop
        this_year = previous_year
        year += 1
