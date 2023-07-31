import utils

path = '../data/operations.json'

# Все операции типе list
operations_list = utils.get_operations_data(path)

# Операции с датой и статусом EXECUTED
filtered_operations_list = utils.data_filtering(operations_list)

# Операции отсортированы по дате
sorted_operations_list = utils.data_sorting(filtered_operations_list)

# Вывод последних 5 операций
for i in range(5):
    transaction = utils.show_transactions(sorted_operations_list[i])
    print(transaction)
    print()
