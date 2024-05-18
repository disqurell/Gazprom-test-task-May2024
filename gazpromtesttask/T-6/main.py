import requests
from requests.exceptions import HTTPError
from logic.helper import Helper


def main():
    helper = Helper()

    try:
        response = requests.get(helper.make_url())

        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
    else:
        data = response.json()

        if not helper.validate_input(data):
            return "Incorrect input data"

        helper.make_df()
        helper.rename_columns()
        helper.add_load_dt()

        return helper.get_result()


if __name__ == "__main__":
    print(main())
