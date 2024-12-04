from scrape_1 import get_company_name_logo
from scrape_2 import insert_data


def main():
    # Filter 1: scrape the data
    data = get_company_name_logo()

    # Filter 2: insert the data in db
    insert_data(data)

if __name__ == "__main__":
    main()
