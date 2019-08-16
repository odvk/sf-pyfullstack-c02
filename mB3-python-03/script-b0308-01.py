# B3.8 Наследование

# классы сами по себе тоже умеют наследовать друг у друга, причем не только атрибуты, но и методы.

# Это значит, что родительские атрибуты и методы будут доступны у так называемых дочерних классов.
# Давайте убедимся в этом. Чтобы задать родительский класс, надо указать его в скобках при объявлении класса,
# как будто это аргумент функции:

import datetime


class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print("eggs.max_quantity", eggs.max_quantity)
print("eggs.is_available", eggs.is_available())


# На самом деле здесь произошло ещё более интересное: для создания экземпляра класса Food
# мы использовали конструктор его родительского класса Product.

# Важно, что если мы назовем атрибут или метод так же, как он называется в родительском классе,
# он будет переопределен. Давайте рассмотрим на примере:


