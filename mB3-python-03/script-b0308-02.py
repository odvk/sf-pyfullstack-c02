# B3.8 Наследование

# классы сами по себе тоже умеют наследовать друг у друга, причем не только атрибуты, но и методы.

# Это значит, что родительские атрибуты и методы будут доступны у так называемых дочерних классов.
# Давайте убедимся в этом. Чтобы задать родительский класс, надо указать его в скобках при объявлении класса,
# как будто это аргумент функции:

# На самом деле здесь произошло ещё более интересное: для создания экземпляра класса Food
# мы использовали конструктор его родительского класса Product.

# Важно, что если мы назовем атрибут или метод так же, как он называется в родительском классе,
# он будет переопределен. Давайте рассмотрим на примере:


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)

"""
Мы видим, что мы: 

1. Переопределили конструктор класса. Теперь мы используем не родительский, а свой, 
и передаём в него другой набор аргументов. Так у нас получился кастомизированный набор атрибутов: 
у родительского класса нет атрибута number_of_views.
2. Переопределили значение атрибута type с помощью атрибута класса. 
Теперь при вызове type от экземпляра нашего дочернего класса мы получим значение атрибута type нашего класса ItemViewEvent.
3. Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.

"""

# Функция isintance.

# Она работает просто: вы передаете в нее объект и тип (класс),
# а она возвращает логическое значение результата проверки, является ли объект объектом нужного вам типа (класса).


print(isinstance("foo", str))
print(isinstance(test_view_event, ItemViewEvent))

# Но у этого метода есть загвоздка:
print(isinstance(test_view_event, Event))

# Мы видим, что для родительского класса она также вернёт True.
# На самом деле, по этой и ряду других причин не всегда хорошо завязывать логику на проверку типа через isinstance.

print(isinstance("foo", object))

