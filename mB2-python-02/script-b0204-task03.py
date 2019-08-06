# Задание 3

# Напишите программу, которая вычисляет произведение чисел, записанных по одному
# в каждой строке файла number.txt, и выводит его на экран.

FILENAME = "numbers.txt"

file_object = open(FILENAME)
product = 1

for line in file_object:
    number = int(line)
    product *= number

print(product)
