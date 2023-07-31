from src.change_data_format import change_date
from datetime import datetime
import pytest


@pytest.mark.parametrize('test_date_list, expected', [
    ({'date': datetime(2020, 10, 3, 5)}, {'date': '03.10.2020'}),
    ({'date': datetime(2012, 3, 5)}, {'date': '05.03.2012'}),
    ({'date': datetime(2022, 12, 12, 12, 12, 12, 12)}, {'date': '12.12.2022'})
])
def test_change_date(test_date_list, expected):
    assert change_date(test_date_list) == expected
