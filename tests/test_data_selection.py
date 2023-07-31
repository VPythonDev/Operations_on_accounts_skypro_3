from src.utils.data_selection import data_filtering


def test_data_filtering():
    test_data = [
        {"date": "2019-04-04T23:20:05.206878", "state": "EXECUTED"},
        {"date": '', "state": "EXECUTED"},
        {"date": "2019-07-12T20:41:47.882230", "state": "CANCELED"},
        {},
        {"date": "", "state": ""}
    ]

    expected = [{"date": "2019-04-04T23:20:05.206878", "state": "EXECUTED"}]

    assert data_filtering(test_data) == expected
