from unittest.mock import patch

import pandas as pd
import pytest


@pytest.fixture
def operations_data():
    data = {
        "Дата операции": ["01.05.2020 16:55:48", "02.05.2020 17:00:05"],
        "Дата платежа": ["02.05.2020", "04.05.2020"],
        "Статус": ["OK", "FAILED"],
    }
    return data


@pytest.fixture(autouse=True)
def mock_read_csv_pandas(operations_data):
    with patch.object(pd, "read_csv") as mock:
        mock.return_value = pd.DataFrame(operations_data)
        yield mock
