# Положим в текущей директории расположен файл user.txt
# Выведем на экран информацию об этом пользователе:

# импортируем модуль стандартной библиотеки json
import json
 # открываем файл на чтение
file_object = open("user.txt")
# загружаем JSON документ с помощью функции load
user = json.load(file_object)
file_object.close()
# теперь в переменной user хранится словарь
print(user)
#{"name": "Monty Python", "gender": "male", "age": 24}
# мы можем работать с этим объектом
print(user["age"])
print(user["name"])
print(user["gender"])
