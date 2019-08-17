# В3.9 Другие способы создания классов

# Мы уже работали со стандартным модулем collections, когда использовали Counter и defaultdict.
# Кроме этого он содержит полезную структуру данных — именованный кортеж, или named tuple.
#
# Эта структура данных очень напоминает класс: сначала вы задаете нужные поля, затем заполняете их.

from collections import namedtuple

User = namedtuple("User", ["name", "age", "email"])

# Здесь мы создали именованный кортеж. Первым аргументом мы передаём его название, вторым — список атрибутов.
# Точно так же, как при определении класса, вы получаете заготовку, которую надо наполнить данными.

# Создадим нашего пользователя:
peter = User(name="Peter", age=32, email="peterrobertson@mail.com")

print(peter.name)

# Другое достоинство хранения данных в именованном кортеже по сравнению, например,
# со словарем состоит в том, что вы не ошибетесь при вызове атрибута:
# если название ключа вы вводите самостоятельно, то при вводе атрибута вы можете
# пользоваться автозаполнением, которое работает в большинстве IDE.

# Таким образом, если вам не требуется наследование или дополнительные возможности,
# предоставляемые классами, но при этом вы хотите хранить объекты со строгой именованной структурой,
# удобно использовать именно именованные кортежи.

print('-----------------------------')
# Вот еще один пример.
from math import sqrt

Point = namedtuple("Point", ["x", "y"])
p1 = Point(1, 2)
p2 = Point(1, 5)

distance = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
print(distance)


# После того, как вы осваиваете работу с классами,
# иногда возникает соблазн использовать их там, где это может быть излишне.

