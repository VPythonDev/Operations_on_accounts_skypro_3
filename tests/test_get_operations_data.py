from src.utils.get_operations_data import get_operations_data
import json


def test_get_operations_data(mocker):
    expected = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
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
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {}
    ]
    # Мок-объект для открытия файла
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(expected)))

    # Вызываем тестируемую функцию
    result = get_operations_data('data/operations.json')

    # Проверяем результат
    assert result == expected
    # Проверяем, что функция open вызывалась с правильными аргументами
    mock_open.assert_called_once_with('data/operations.json', 'r')
