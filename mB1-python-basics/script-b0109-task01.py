# Ветвление. if. Циклы while


# Практическое задание 1.
# Дополните код так, чтобы он выводил только те имена, которые начинаются на гласную букву.
names = ["Константин", "Александр", "Ирина", "Григорий", "Олег", "Екатерина", "Дарья", "Юрий"]
vowels = ["А", "Я", "Э", "Е", "И", "О", "Ё", "У", "Ю"]
i = 0
while i < len(names):
    if names[i][0] in vowels:
        print(names[i])
    i = i + 1
print()
print()

# Практическое задание 2.
# Какой кот потеряется при выводе на экран?
cats = ["Пушистик", "Рыжик", "Урчалка", "Ариша", "Василий", "Бегемот"]
i = 0
while i != len(cats) - 1:
    i = i + 1
    print(cats[i])