def change_date(operation_data):
    """Изменяет формат даты на ДД.ММ.ГГГГ"""
    operation_data['date'] = operation_data['date'].strftime("%d.%m.%Y")
    return operation_data
