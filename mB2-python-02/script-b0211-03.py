# B2.11 Модуль collections: defaultdict и Counter
# В этом уроке мы остановимся на двух новых для нас контейнерах: defaultdict и Counter.

# Класс Counter является частным случаем класса defaultdict: тип фабрики значений для отсутствующих ключей — int.
# Как нетрудно догадаться, класс Counter удобно использовать для всевозможных подсчетов.
# Рассмотрим примеры аналогичные приведенным выше для defaultdict:


import collections

print("-- 1 ------------------")

c = collections.Counter()
print(c["key"])
print(c["k"])
c[42] += 1
print(c[42])
print(c)

# Эти примеры демонстрируют идентичность интерфейса Counter с интерфейсом класса defaultdict(int).
# Однако у класса Counter есть специфичный метод most_common. С его помощью можно получить заданное количество
# самых популярных (с наибольшим значением счетчика) элементов.
# Метод most_common возвращает список пар (ключ, значение).

print("-- 2 ------------------")
# import collections  # импортируем модуль collections
import random  # импортируем модуль random

c = collections.Counter()  # заводим пустой счетчик
for x in range(50):  # заполняем счетчик
    c[x] = random.randint(1, 100)  # произвольными значениями от 1 до 100
print(c)  # посмотрим что получилось
print(c.most_common(3))  # выводим список 3 самых популярных пар (ключ, значение)
for key, value in c.most_common(3):
    print("{} - {}".format(key, value))

# Класс Counter удобно использовать для подсчета частоты символов в строке — можно передать строку
# как первый аргумент, при создании счетчика, все остальное будет сделано за нас.
print("-- 3 ------------------")

# import collections  # импортируем модуль collections
a_string = "Calculate frequency of characters in this string"  # строка
c = collections.Counter(a_string) # указываем строку, как аргумент класса Counter
print(c) # за нас подсчитана частота каждого символа в строке
print(c.most_common(2)) # выводим 2 наиболее популярных символа вместе с частотами
