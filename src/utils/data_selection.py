def data_filtering(operations_data_list):
    """Возвращает список транзакций по статусу перевода и наличии не пустой даты"""
    filtered_operations_list = []

    for transaction_data in operations_data_list:
        if transaction_data.get("state") and transaction_data.get('date'):
            if transaction_data["state"] == "EXECUTED":
                filtered_operations_list.append(transaction_data)

    return filtered_operations_list
