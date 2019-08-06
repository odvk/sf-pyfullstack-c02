# Метод dump позволяет решить обратную задачу: сохранить на диск объект словаря Python в виде JSON-документа.
# Перейдем к примерам:

# импортируем модуль стандартной библиотеки json
import json

# создаем словарь с данными пользователя
user = {"name": "Monty Python", "gender": "male", "age": 24}
# открываем на запись файл user.txt
file_object = open("user.txt", "w")
# сохраняем словарь user в объект файла file_object
json.dump(user, file_object)
# закрываем объект файла
file_object.close()

# Аналогично можно создать файл со списком клиентов:
customers = [{"name": "Alice", "gender": "female", "email": "alice@example.com"},
             {"name": "Bob", "gender": "male", "email": "bob24@exa.net"},
             {"name": "John", "gender": "female", "email": "john@johnjefferson.org"}]
file_object = open("customers01.txt", "w")
json.dump(customers, file_object)
file_object.close()
