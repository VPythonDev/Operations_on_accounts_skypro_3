from src.utils.sorting import data_sorting
from datetime import datetime


def test_data_sorting():
    test_date_list = [
        {"date": "2018-11-08T22:47:21.935582"},
        {"date": "2019-12-04T22:47:21.935582"},
        {"date": "2018-12-06T22:50:21.935582"},
        {"date": "2019-12-04T22:46:21.935582"}
    ]
    expected = [
        {"date": datetime(2019, 12, 4, 22, 47, 21, 935582)},
        {"date": datetime(2019, 12, 4, 22, 46, 21, 935582)},
        {"date": datetime(2018, 12, 6, 22, 50, 21, 935582)},
        {"date": datetime(2018, 11, 8, 22, 47, 21, 935582)}
    ]

    assert data_sorting(test_date_list) == expected
