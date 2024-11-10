from selenium.webdriver.common.by import By
import sqlite3

def insert_from_table_to_db(driver, issuer_code: str):
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    table_data = []
    for row in rows:
        # Extract each cell in the row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Get text content from each cell
        cell_data = [cell.text for cell in cells]
        if cell_data:  # Avoid empty rows
            table_data.append(cell_data)

        driver.quit()

        conn = sqlite3.connect("scraped_data.db")
        cursor = conn.cursor()

        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS data_table_{issuer_code} (
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

        for data in table_data:
            sql_code = f"INSERT INTO data_table_{issuer_code}" \
                       "(Transaction_Date, Price_Of_Last_Transaction, Max, Min, Average_Price, %Change, Quantity, Turnover_BEST_denars, Total_Turnover_denars)" \
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,)"
            cursor.execute(sql_code, data)

        conn.commit()
        conn.close()
