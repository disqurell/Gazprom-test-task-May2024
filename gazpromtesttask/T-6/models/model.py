from pydantic import BaseModel, field_validator
from datetime import datetime


class FromHTTPData(BaseModel):
    Columns: list[str]
    Description: str
    RowCount: int
    Rows: list

    @field_validator("Rows")
    @classmethod
    def check_types(cls, data: list) -> list:
        for lst in data:
            try:
                datetime.fromisoformat(lst[1])
            except Exception:
                raise ValueError("Incorrect date")
            if lst:
                if not (isinstance(lst[0], int) and isinstance(lst[2], str)):
                    raise ValueError("Incorrect types in Rows")

        return data
