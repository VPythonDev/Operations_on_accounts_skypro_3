from datetime import datetime


def data_sorting(transactions_list):
    """Переводит дату в объект datetime и сортирует список по дате"""
    for transaction_data in transactions_list:
        transaction_data['date'] = datetime.strptime(transaction_data['date'], "%Y-%m-%dT%H:%M:%S.%f")

    sorted_transactions_list = sorted(transactions_list, key=lambda transaction: transaction['date'], reverse=True)

    return sorted_transactions_list
