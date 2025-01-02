from datetime import datetime
from typing import Any
from unittest.mock import patch

from src.external_api import conversion_currency
from src.utils import get_transactions


def test_get_greeting() -> Any:
    return datetime(2020, 5, 1, 4, 1, 1)


@patch("requests.get")
def test_get_transactions_rub(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}

    assert get_transactions(transaction) == 100


@patch("requests.get")
def test_get_transactions_usd(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1000}

    assert get_transactions(transaction) == 1000


@patch("src.external_api.requests.request")
def test_get_sum(mock_get):
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 20, "from": "USD", "to": "RUB"},
        "result": 3724.305775,
        "success": True,
    }

    assert conversion_currency == []
