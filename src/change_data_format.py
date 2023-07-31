def change_date(operation_data):
    """Изменяет формат даты на ДД.ММ.ГГГГ"""
    changed_date = operation_data['date'].strftime("%d.%m.%Y")
    return changed_date


def hide_sender_number(operation_data):
    """Скрывает номер карты отправителя"""
    sender_number = operation_data['from'].split()[-1]
    hidden_sender_number = sender_number.replace(sender_number[6:-4], '*' * len(sender_number[6:-4]))

    # Ставит пробел через каждые 4 символа в hidden_sender_number
    for i in range(-4, -len(hidden_sender_number), -5):
        hidden_sender_number = hidden_sender_number[:i] + ' ' + hidden_sender_number[i:]

    return hidden_sender_number
