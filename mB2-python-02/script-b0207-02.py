# Рассмотрим теперь пример файла customers.txt, в котором хранится список клиентов интернет-магазина:
# Выведем на экран информацию о пользователях женского пола:

# импортируем модуль стандартной библиотеки json
import json

# открываем файл customers.txt на чтение
file_object = open("customers.txt")
# загружаем JSON документ с помощью функции load
customers = json.load(file_object)
file_object.close()
# в переменной customers теперь хранится список
print(customers)
# выведем на экран первый элемент этого списка
# print(customers[0])
print()
# С помощью цикла for итерируемся по списку customers
for customer in customers:
    # проверяем значение поля gender на равенство строке female
    if customer['gender'] == "female":
        # распечатываем на экран
        print(customer)
