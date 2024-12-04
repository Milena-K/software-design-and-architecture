from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import time

def get_company_name_logo():
    base_url = "https://www.mse.mk"
    response = requests.get(base_url + "/mk/issuers/shares-listing")

    table_ids = ["super-table", "exchange-table", "mandatory-table"]
    table_data = []
    for tID in table_ids:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id={tID})
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all(['td'])
            cells = cells[:2]
            row_data = []

            first_cell = True
            for cell in cells:
                if first_cell:
                    try:
                        row_data.append(cell.find('img')['src'])
                        first_cell = False
                    except:
                        pass
                else:
                    row_data.append(cell.get_text(strip=True))
                    try:
                        row_data.append(cell.find('a')['href'])
                    except:
                        pass
            if row_data:
                table_data.append(row_data)

    return table_data
