# B2.12 Разделение и объединение строк

# Текстовые данные в Python представляются в виде str объектов (strings).
# Строковые объекты являются !!неизменяемыми!! последовательностями юникодных символов.

# При работе со строками часто возникает необходимость разделять (split) и объединять (join) строковые литералы.
# Для этого в Python предусмотрены специальные методы: str.split и str.join. Рассмотрим их подробнее.

# Метод split() возвращает список слов исходной строки, разделенных любым количеством пробелов
# или символов переноса строки. Рассмотрим несколько примеров:

s = "split me"
print(s)
print(s.split())

s = "split       me      "
print(s)
print(s.split())

s = "\nsplit\n\n\n   me\n"
print(s)
print(s.split())

print("-----------------")

# Метод join() принимает на вход контейнер строк и возвращает строку, полученную в результате их конкатенации.
# В качестве разделителя между элементами используется строка, предоставляющая этот метод.
# Рассмотрим несколько примеров:

# Создаем список слов
words = ["Monty", "Python\'s", "flying", "circus"]
# Объединяем их в предложение, склеивая список words с помощью пробела
sentence = " ".join(words)
# Распечатываем результат на экран
print(sentence)

print("-----------------")
# Попробуем теперь объединить в строку список фруктов:
# Создаем список фруктов
fruits = ["apple", "peach", "pineapple", "banana"]
# Объединяем фрукты через запятую
fruits_string = ", ".join(fruits)
# Посмотрим что у нас получилось
print(fruits_string)

print("-----------------")
# Вернемся к нашему списку фруктов и попробуем распечатать на экран рецепт фруктового салата:
fruits = ["apple", "peach", "pineapple", "banana"]
sentence = "My favorite fruit salad consists of " + ", ".join(fruits)
print(sentence)

print("-----------------")
# Попробуем теперь решить синтетическую задачу, которая тем не менее,
# поможет нам запомнить особенности работы с методами split и join.
# Составить строку s из слов строки sentence, разделенных символом "+".

# Исходная строка
sentence = "Pretty long sentence with whitespaces as word delimiter."
# Разделяем исходную строку по словам
words = sentence.split()
# Распечатаем полученный список
print(words)
# Объединяем полученный список слов в строку
resulting_string = "+".join(words)
print(resulting_string)
