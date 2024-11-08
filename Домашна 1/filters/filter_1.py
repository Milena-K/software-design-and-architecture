from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def get_issuers():
    driver = webdriver.Chrome()
    driver.get("https://www.mse.mk/mk/stats/symbolhistory/kmb")
    dropdown = driver.find_element(By.ID, "Code")
    options = dropdown.find_elements(By.TAG_NAME, "option")

    # Filter the codes that don't contain numbers
    valid_codes = [option.text for option in options if re.match("^[A-Za-z]+$", option.text)]
    driver.quit()
    return valid_codes

