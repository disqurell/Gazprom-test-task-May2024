# Readme for T-6

## To run script:
1. Install poetry
2. Create `.env` file with api link:
```python
API_URL=""
```
3. Cd to `.../GazpromTestTask/gazpromtesttask/T-6` and run:
```sh
poetry shell && poetry install;

poetry run python3 main.py
```

## To test T-6 (without API call):
1. Replace the code in the `main.py` with:
```python
import json
from datetime import datetime
from logic.helper import Helper


test_data = {
    "Columns": ["key1", "key2", "key3"],
    "Description": "Банковское API каких-то важных документов",
    "RowCount": 2,
    "Rows": [[23, str(datetime.now()), "value3"], [24, str(datetime.now()), "value6"]],
}


def main():
    helper = Helper()

    data = json.dumps(test_data)

    if not helper.validate_input(data):
        return "Incorrect input data"

    helper.make_df()
    helper.rename_columns()
    helper.add_load_dt()

    return helper.get_result()
```

2. [Run script](#to-run-script)