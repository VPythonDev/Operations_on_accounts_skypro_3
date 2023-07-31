import pytest
from datetime import datetime
from src.display_transactions import show_transactions


@pytest.mark.parametrize('test_transaction, expected', [
    ({
    "id": 441945886,
    "state": "EXECUTED",
    "date": datetime(2020, 3, 3),
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }, """03.03.2020 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб."""),
    ({
    "id": 587085106,
    "state": "EXECUTED",
    "date": datetime(2018, 3, 23),
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }, """23.03.2018 Открытие вклада
 -> Счет **2431
48223.05 руб.""")
])
def test_show_transactions(test_transaction, expected):
    assert show_transactions(test_transaction) == expected
