# B2.8 Модуль random и угадай число на Python

# Используем функцию random.randint для реализации уже знакомой нам игры “Угадай число” на Python.
# Сравните её с реализацией этой игры на JavaScript в уроке A5.9.

# Вспомним формальные условия задачи. У нас есть целое число на отрезке от 1 до 100,
# у пользователя есть 10 попыток, чтобы его угадать. Если число, выбранное пользователем,
# меньше или больше загаданного, выводим соответствующее сообщение и количество оставшихся попыток.


# ----------  Вариант 1  ---- число в файле
# В переменной хранится имя файла с секретом
# FILENAME = 'secret.txt'
# Открываем файл на чтение
# secret_file = open(FILENAME)
# Читаем содержимое файла
# secret = secret_file.read().strip()
# Приводим полученную строку к типу int
# secret = int(secret)

# ----------  Вариант 2  ---- случайное число

import random

secret = random.randint(1, 100)

# ---
for attempt in range(10, 0, -1):
    # cохраняем в переменную guess ввод пользователя
    guess = input('Угадай загаданное число, у тебя {} попыток. '.format(attempt))
    # функция input вне зависимости от ввода пользователя, возвращает строку, поэтому ее нужно привести к типу int
    guess_number = int(guess)
    # если пользователь угадал загаданное число
    if guess_number == secret:
        # выводим на экран соответствующее сообщение и выходим из цикла
        print('Верно!')
        break
    # если же пользователь ошибся, распечатываем подсказку и продолжаем цикл
    elif guess_number < secret:
        print('Я загадал число больше, попробуй еще раз.')
    else:
        print('Я загадал число меньше, попробуй еще раз.')
