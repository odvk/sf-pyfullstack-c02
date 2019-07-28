i = 5
while i != 0:
    print("Eggs!")
    i = i - 1

print("Задание. Давайте наполним список остатками от деления числа на значение счётчика.")
i = 5
residuals = []
while i != 0:
    residuals.append(11 % i)
    i = i - 1

print(residuals)