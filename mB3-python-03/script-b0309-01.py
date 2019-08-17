# В3.9 Другие способы создания классов

# Давайте посмотрим, как ещё можно управлять состоянием экземпляров класса.

class Number:
    value = 4


num = Number()
setattr(num, "value", 6)
print(getattr(num, "value"))

print('--------------------------------')

# На практике название атрибута в конкретный момент времени может быть неизвестно,
# а благодаря этому синтаксису мы можем создавать атрибуты динамически.
# Например, мы можем создать объект класса с полями, которые мы получим из списка:

class User:
    pass


user1 = [
    "Peter",
    "32",
    "peterrobinson@mail.com",
    ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
]

attrs = ["name", "age", "email", "purchases"]
user_instance = User()
for attr, val in zip(attrs, user1):
    setattr(user_instance, attr, val)
    print(getattr(user_instance, attr))

# Мы использовали встроенную функцию zip() для того, чтобы итерироваться по двум спискам одновременно,
# и создавали атрибуты динамически.
print('---')
print(user_instance.purchases)
print(getattr(user_instance, "purchases"))

