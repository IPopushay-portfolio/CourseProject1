from black import datetime

from src.utils import filter_by_date, get_operations
from src.views import main_page


def main():
    df = get_operations()
    df = filter_by_date(df, datetime(2020, 5, 20))
    print(df)

    response = main_page("2020-05-20")
    print(response)
