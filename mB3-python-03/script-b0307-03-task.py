# В3.7 Ещё раз про “магические” методы

"""
Определите класс NutritionInfo в окошке внизу со всеми необходимыми методами:

1. Не используйте принты, грейдер их не читает.
2. Вам нужно будет определить специальные методы. Ориентируйтесь на строчку выше где мы получили переменную "breakfast" из двух яблок и одного творога.
3. Два яблока это одно яблоко умноженное на число два
4. Два яблока и творог это яблоко умноженное на число два плюс творог
5. Творог и яблоко это объекты класса NutrtitionInfo. Именно у этого класса надо определить специальные методы чтобы их можно было складывать и умножать
6. Чтобы у результата суммы двух NutritionInfo был метод energy, результат сложения должен быть тоже NutritionInfo.
7. Чтобы результат умножения NutritionInfo на число можно было потом сложить с другим объектом NutritionInfo, результат умножения должен быть тоже NutritionInfo.
8. Самый простой способ сделать оба пункта выше – в сложении и умножении создавать новый объект с новыми значениями, и возвращать его.

Это задание кажется простым по описанию, но может оказаться в реальности довольно сложным.
Помните про возвращение (return) из специальных методов.
Не паникуйте, если вдруг задание даётся не сразу.
"""


class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def __mul__(self, other):
        return NutritionInfo(self.proteins * 2, self.carbs * 2, self.fats * 2)

    def __rmul__(self, other):
        return NutritionInfo(self.proteins * 2, self.carbs * 2, self.fats * 2)

    def __add__(self, other):
        return NutritionInfo(self.proteins + other.proteins, self.carbs + other.carbs, self.fats + other.fats)

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)


# Определяем яблоко и 9% творог:

tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)

print('Творог: ', tvorog_9.energy())
print('Яблоко: ', apple.energy())

print('Яблоко*2: ', (apple *2).energy())

# А вот так мы можем посчитать энергетическую ценность завтрака из творога и двух яблок:
breakfast = apple * 2 + tvorog_9
print('apple * 2 + tvorog_9: ', breakfast.energy())
