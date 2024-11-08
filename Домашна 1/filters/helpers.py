from selenium.webdriver.common.by import By
from selenium import webdriver

def insert_from_table_to_db():
    driver = webdriver.Chrome()
    driver.get("https://www.mse.mk/mk/stats/symbolhistory/kmb")
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

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data_table (
                Transaction_Date DATE,
                Price_Of_Last_Transaction REAL,
                Max REAL,
                Min REAL,
                Average_Price REAL,
                %Change REAL,
                Quantity INTEGER,
                Turnover_BEST_denars INTEGER,
                Total_Turnover_denars INTEGER
            )
        """)

        for data in table_data:
            cursor.execute(
                """INSERT INTO data_table
                (Transaction_Date, Price_Of_Last_Transaction, Max, Min, Average_Price, %Change, Quantity, Turnover_BEST_denars, Total_Turnover_denars)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,)""",
                data
            )

        conn.commit()
        conn.close()
