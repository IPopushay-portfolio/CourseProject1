import datetime

import pandas as pd

from src.config import BASE_DIR

OPERATION_PATH = BASE_DIR.joinpath("data", "operations.csv")


def spending_by_category(transactions: pd.DataFrame, category: str, date) -> pd.DataFrame:
    df = pd.read_csv(OPERATION_PATH)
    if date is None:
        date = datetime.timedelta()
    else:
        date = datetime.datetime.strptime(date, __format="%d.%m.%Y")
    transactions["Дата операции"] = pd.to_datetime(
        transactions["Дата операции"], format="%d.%m.%Y %H:%M:%S", errors="coerce"
    )

    filtered_transactions = transactions.loc[
        (transactions["Категория"] == category)
        & (date.month == transactions["Дата операции"].dt.month <= 3)
        & (date.year == transactions["Дата операции"].dt.year)
    ]
    filtered_transactions.loc[:, "Дата операции"] = filtered_transactions["Дата операции"].dt.strftime(
        "%d.%m.%Y %H:%M:%S"
    )
    for t in filtered_transactions.to_dict(orient="records"):
        return t
    return df
