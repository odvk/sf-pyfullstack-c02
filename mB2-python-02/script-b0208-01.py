# B2.8 Модуль random и угадай число на Python

# random.randint(а, b)
# Возвращает случайное целое число на отрезке [a, b],
# то есть полученное число будет больше или равно a и меньше или равно b.

# random.random()
# Возвращает случайное вещественное число на промежутке [0.0, 1.0),
# то есть полученное число будет больше или равно 0.0 и строго меньше 1.0.

# random.choice(sequence)
# Возвращает случайный элемент непустого контейнера sequence (списка, кортежа, строки).

import random
alist = [1, 2, 3, 4, 5, 6, 'word']
print(random.choice(alist))
print(random.choice(alist))
print(random.choice(alist))
print(random.choice(alist))
print(random.choice(alist))
print()

atuple = ('word', 5, 4, 3, 2, 1)
print(random.choice(atuple))
print(random.choice(atuple))
print(random.choice(atuple))
print()

astring = 'String is a sequence too, by the way'
print(random.choice(astring))
print(random.choice(astring))
print(random.choice(astring))
print(random.choice(astring))
