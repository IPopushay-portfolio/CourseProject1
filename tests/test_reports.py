from black import datetime

from src.utils import filter_by_date, get_operations


def test_one(mock_read_csv_pandas):
    df = get_operations()
    result = filter_by_date(df, datetime(2020, 5, 1))
    assert len(result) == 1
    assert result["Дата операции"] == "2020-05-02"
