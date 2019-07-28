# B1.10 Цикл for

#1 сумма четных элементов
numbers = [-8, 3, 4, 20, -55, 111, 168, 19]
sum_ = 0

for number in numbers:
    if number % 2 != 0:
        sum_ = sum_ + number

print(sum_)

#2 Давайте в качестве следующего примера найдём минимальный элемент в массиве.
numbers = [-8, 3, 4, 20, -55, 111, 168, 19]
min_ = numbers[0]

for number in numbers:
    if number < min_:
        min_ = number
print(min_)

#3. Если вы хотите исполнить набор команд конкретное число раз
for number in range(10):
    print(number)