import json

path = "data/operations.json"


def get_operations_data():
    """Возвращает данные операций из файла operations.json"""
    with open(path, 'r') as operations_data_file:
        operations_data = json.load(operations_data_file)
    return operations_data
