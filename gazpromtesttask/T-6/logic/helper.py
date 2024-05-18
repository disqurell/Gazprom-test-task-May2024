from config import API_URL
from datetime import datetime, timezone
from models.model import FromHTTPData
import pandas as pd


class Helper:

    def __init__(self) -> None:
        self.dict_data = None
        self.df = None

    def make_url(self):
        day_start = int(
            datetime.now(timezone.utc)
            .replace(hour=0, minute=0, second=0, microsecond=0)
            .timestamp()
        )

        return API_URL + f'very/important/docs?documents_date={f"{day_start}"}'

    def validate_input(self, input_data: dict):
        try:
            self.dict_data = FromHTTPData.model_validate_json(input_data)
            return True
        except Exception as e:
            print(e)
            return False

    def make_df(self):
        columns = self.dict_data.Columns
        rows = [[row[i] for i in range(len(row))] for row in self.dict_data.Rows]

        self.df = pd.DataFrame(rows, columns=columns)

    def rename_columns(self):
        self.df = self.df.rename(
            columns={
                "key1": "document_id",
                "key2": "document_dt",
                "key3": "document_name",
            }
        )

    def add_load_dt(self):
        self.df["load_dt"] = datetime.now()

    def get_result(self):
        return self.df
