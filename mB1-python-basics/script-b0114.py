# B1.14 Домашнее задание

# У вас есть словарь словарей со значениями длины и ширины чашелистника и длины лепестков разных цветов.
# Ключом во внешнем словаре является название цветка. Посчитайте средний размер каждого параметра для всех цветов вместе.
# Получившиеся значения введите в форму ниже. Расчёт каждой величины можно сделать в одну строчку,
# но так как это не увеличит читаемость, можно использовать дополнительные переменные.

# При решении обратите внимание, что среднее средних не равняется общему среднему значению.

flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
        "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
        "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

# выше были данные, а после этой строчки
# вам надо дописать код.


# общее среднее значение для sepal_length:
mean_sepal_length = 0
# общее среднее значение для sepal_width:
mean_sepal_width = 0
# общее среднее значение для petal_length:
mean_petal_length = 0

# ------Вариант 1
sepal_length_list = []
sepal_width_list = []
petal_length_list = []

for flower, parameters in flowers.items():
    for parameter, numbers in parameters.items():
        # print(parameter, numbers)
        if parameter == "sepal_length":
            for number in numbers:
                sepal_length_list.append(number)
        if parameter == "sepal_width":
            for number in numbers:
                sepal_width_list.append(number)
        if parameter == "petal_length":
            for number in numbers:
                petal_length_list.append(number)

mean_sepal_length = sum(sepal_length_list) / len(sepal_length_list)
mean_sepal_width = sum(sepal_width_list) / len(sepal_width_list)
mean_petal_length = sum(petal_length_list) / len(petal_length_list)
print(round(mean_sepal_length, 1), round(mean_sepal_width, 1), round(mean_petal_length, 1))


# ------Вариант 2
def find_mean(target_dict, parameter):
    all_parameters = []
    for each in target_dict:
        all_parameters.extend(target_dict[each][parameter])
        # print(all_parameters)
    summ = sum(all_parameters)
    mean = summ / len(all_parameters)
    print('mean_' + parameter, round(mean, 1))


find_mean(flowers, 'sepal_length')
find_mean(flowers, 'sepal_width')
find_mean(flowers, 'petal_length')

# ------Вариант 3
sepal_length_list = []
sepal_width_list = []
petal_length_list = []

for flower in flowers:
    sepal_length_list.extend(flowers[flower]["sepal_length"])
    sepal_width_list.extend(flowers[flower]["sepal_width"])
    petal_length_list.extend(flowers[flower]["petal_length"])
# общее среднее значение для sepal_length:
mean_sepal_length = round(sum(sepal_length_list) / len(sepal_length_list), 1)
# общее среднее значение для sepal_width:
mean_sepal_width = round(sum(sepal_width_list) / len(sepal_width_list), 1)
# общее среднее значение для petal_length:
mean_petal_length = round(sum(petal_length_list) / len(petal_length_list), 1)
print("""Средняя длина: %s 
    Средняя ширина: %s
    Средняя длина лепестков: %s""" % (mean_sepal_length, mean_sepal_width, mean_petal_length))

# ------Вариант 4
s_l = []
s_w = []
p_l = []

for fl in flowers.values():
    s_l += fl['sepal_length']
    s_w += fl['sepal_width']
    p_l += fl['petal_length']

print(sum(s_l) / len(s_l))
print(sum(s_w) / len(s_w))
print(sum(p_l) / len(p_l))

# ------ Вариант 5. Разбор задания от кураторов
print("Вариант 5. Разбор задания от кураторов")
sepal_length_list = []
sepal_width_list = []
petal_length_list = []

for flower, data in flowers.items():
    for length in data["sepal_length"]:
        sepal_length_list.append(length)

    for width in data["sepal_width"]:
        sepal_width_list.append(width)

    for length in data["petal_length"]:
        petal_length_list.append(length)

mean_sepal_length = sum(sepal_length_list) / len(sepal_length_list)
mean_sepal_width = sum(sepal_width_list) / len(sepal_width_list)
mean_petal_length = sum(petal_length_list) / len(petal_length_list)
print(round(mean_sepal_length, 1), round(mean_sepal_width, 1), round(mean_petal_length, 1))
