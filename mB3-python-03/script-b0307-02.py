# В3.7 Ещё раз про “магические” методы

"""
Представим, что мы разрабатываем сервис для подсчёта калорий, белков, жиров и углеводов.
Для этого нам нужно создать классы, которые делают базовую арифметику сложения между элементами,
чтобы получить общее количество элементов и калорий в многокомпонентных блюдах.
"""


# Определим класс, который сохраняет объект с характеристиками:

class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)


# Определяем яблоко и 9% творог:

tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)

print('Творог: ', tvorog_9.energy())
print('Яблоко: ', apple.energy())


# А вот так мы можем посчитать энергетическую ценность завтрака из творога и двух яблок:
# breakfast = apple * 2 + tvorog_9
# print(breakfast.energy())


