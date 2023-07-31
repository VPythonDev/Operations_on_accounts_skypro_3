from src.change_data_format import change_date, hide_sender_number
from datetime import datetime
import pytest


@pytest.mark.parametrize('test_date_list, expected', [
    ({'date': datetime(2020, 10, 3, 5)}, '03.10.2020'),
    ({'date': datetime(2012, 3, 5)}, '05.03.2012'),
    ({'date': datetime(2022, 12, 12, 12, 12, 12, 12)}, '12.12.2022')
])
def test_change_date(test_date_list, expected):
    assert change_date(test_date_list) == expected


@pytest.mark.parametrize('test_sender_nums, expected', [
    ({'from': 'Visa Gold 5999414228426353'}, '5999 41** **** 6353'),
    ({'from': '1111222233334444'}, '1111 22** **** 4444')
])
def test_hide_sender_number(test_sender_nums, expected):
    assert hide_sender_number(test_sender_nums) == expected
