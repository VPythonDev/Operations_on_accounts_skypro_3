def change_date(operation_data):
    """Изменяет формат даты на ДД.ММ.ГГГГ"""
    changed_date = operation_data['date'].strftime("%d.%m.%Y")
    return changed_date


def hide_sender_number(operation_data):
    """Скрывает номер карты отправителя"""
    sender_number = operation_data['from'].split()[-1]
    hidden_sender_number = sender_number.replace(sender_number[6:-4], '*' * len(sender_number[6:-4]))
    return hidden_sender_number
