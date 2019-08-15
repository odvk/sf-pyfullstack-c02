# B3.5 Методы

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock
    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


eggs = Product("eggs", "food", 5)
print(eggs.is_available())

# Для вызова метода, как и для вызова функции, используются круглые скобки.
# Разница между методом и функцией только в том, что метод вызывается от конкретного объекта
# и реализован внутри класса, а функция работает сама по себе.


