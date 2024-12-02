
from filter1 import get_issuers
from filter2 import check_last_data
from filter3 import fetch_and_update_data


def main():
    # Filter 1: Get list of issuers
    issuers = get_issuers()

    # Filter 2: Check last available data
    last_data_info = check_last_data(issuers)

    # Filter 3: Fetch missing data and update database
    fetch_and_update_data(last_data_info)

if __name__ == "__main__":
    main()
