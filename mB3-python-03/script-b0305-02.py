# B3.5 Методы

class Event:
    def __init__(self, timestamp, event_type, session_id):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id


events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

# Давайте для каждого события в списке создадим соответствующий ему объект с помощью конструктора,
# как мы уже делали. А чтобы убедиться, что объект создаётся, выведем на печать какой-нибудь из атрибутов:
"""
for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
                      event_type=event.get("type"),
                      session_id=event.get("session_id"))
    print(event_obj.timestamp)
"""


# Для этого давайте поправим объявление нашего класса и зададим для каждой переменной ее значения по умолчанию,
# чтобы мы могли инициализировать объект без заполнения. Это делается с помощью указания
# значений по умолчанию сразу после названия аргумента:
class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")


# После этого мы скрыли реализацию логики от пользователя — то есть нам уже неважно,
# как это работает, мы знаем, что можем подать на вход словарь с нужными ключами, и всё будет работать само.
for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

