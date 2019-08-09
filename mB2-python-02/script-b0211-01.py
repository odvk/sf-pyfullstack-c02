# B2.11 Модуль collections: defaultdict и Counter
# В этом уроке мы остановимся на двух новых для нас контейнерах: defaultdict и Counter.

import collections

# если мы создаем словарь. и пытаемся получить значение по отсутствующему в d ключу key,
# то мы получим пустой объект заданного типа som_type_here.
# d = collections.defaultdict(some_type_here)

# Рассмотрим несколько примеров:
print("1 -----------")
d = collections.defaultdict(list)  # создаем словарь d и указывам list, как фабрику для новых ключей
print(d)  # в переменной d сейчас хранится пустой словарь

print(d["key"])  # выводим значение по ключу key, оно не определено в словаре, поэтому используется значение по умолчанию — пустой список
print(d[42])  # аналогично происходит для любого ключа
print(d)  # в переменной d сейчас хранится пустой словарь

print("2 -----------")
# Подобная особенность позволяет нам работать со словарем типа defaultdict так,
# будто интересующий нас ключ уже есть в словаре:
d["k"].append(33)
print(d)
print(d["k"])


