from src.change_data_format import change_date, hide_sender_number, hide_recipient_number


def show_transactions(transaction_dict):
    """Подготавливает и выводит данные транзакций"""
    date = change_date(transaction_dict)
    description = transaction_dict['description']

    if 'from' in transaction_dict:
        sender_number = transaction_dict['from']
        hidden_sender_number = sender_number.replace(sender_number.split()[-1], hide_sender_number(transaction_dict))
    else:
        hidden_sender_number = ''

    recipient_number = transaction_dict['to']
    hidden_recipient_number = recipient_number.replace(recipient_number.split()[-1], hide_recipient_number(transaction_dict))

    amount = transaction_dict['operationAmount']['amount']
    currency = transaction_dict['operationAmount']['currency']['name']

    output = f"""{date} {description}
{hidden_sender_number} -> {hidden_recipient_number}
{amount} {currency}"""
    return output
