# B2.11 Модуль collections: defaultdict и Counter
# В этом уроке мы остановимся на двух новых для нас контейнерах: defaultdict и Counter.


# Рассмотрим следующую задачу. Дан текстовый файл numbers.txt, содержащий несколько чисел в каждой своей строке.
# Вычислить сумму чисел в каждой строке.
# Для решения этой задачи составим словарь с номерами строк в качестве ключей и суммой чисел соответствующей строки
# — в качестве значений. Приведем листинг программы, решающей поставленную задачу и обсудим его.

import collections  # импортируем модуль collections

FILENAME = "data/numbers1.txt"
#FILENAME = "numbers1.txt"

fp = open(FILENAME)  # открываем файл на чтение

#--- Версия 1
#counter = collections.defaultdict(int)  # создаем счетчик

# line_number = 1  # заводим переменную, для хранения номера текущей строки
# for line in fp:  # итерируемся по строкам исходного файла
#     numbers = line.split()  # получаем список чисел в текущей строке
#     # print(numbers)
#     for number in numbers:  # итерируемся по полученному списку чисел
#         int_number = int(number)  # приводим строковое представление числа к типу int
#         counter[line_number] += int_number  #
#         # print(counter[line_number])
#     line_number += 1  # увеличиваем счетчик строки

#--- Версия 2

counter = collections.defaultdict(int)  # создаем счетчик

line_number = 1  # заводим переменную, для хранения номера текущей строки
for line in fp:  # итерируемся по строкам исходного файла
    numbers = line.split()  # получаем список чисел в текущей строке
    # print(numbers)
    for number in numbers:  # итерируемся по полученному списку чисел
        int_number = int(number)  # приводим строковое представление числа к типу int
        counter[line_number] += int_number  #
        # print(counter[line_number])
    line_number += 1  # увеличиваем счетчик строки


fp.close()  # закрываем файл

for line_num, line_sum in counter.items():  # проходимся по парам ключ-значение счетчика
    print("{} - {}".format(line_num, line_sum))  # распечатываем на экран номер строки и сумму чисел на ней
