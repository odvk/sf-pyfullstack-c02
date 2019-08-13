# B2.14 Парсер журналов событий

# Домашнее задание в этом модуле предполагает работу с журналами интернет-магазина.
# В предыдущем уроке мы рассмотрели пример текстовых журналов и научились отвечать на элементарные вопросы о системе.
# Теперь нам  предстоит обработать журнал событий: чаще всего это просто текстовый файл,
# в каждую строку которого выгружены события из аналитической системы.

# сообщения в таком журнале уже структурированы — в каждой строке файла записан JSON документ
# Логика обработки журналов:
# - прочитать файл по строкам;
# - десериализовать строку в словарь, используя метод json.loads;
# - провести необходимую фильтрацию событий: проверить, что поле detectedDuplicate равно False, поле detectedCorruption равно False, провести дополнительную фильтрацию, необходимую по каждому из пунктов;
# - провести вычисления;
# - вывести полученные результаты на экран.

# В журнале журнал 2 (data_3000.json) есть события с типом itemFavEvent (поле eventType равно itemFavEvent).
# Они появились после того, как в наш интернет-магазин добавили возможность внести товар в избранное
# (то есть пользователь может товар пометить "звёздочкой" или "лайкнуть").
# Модифицируйте программу для построения следующих метрик по избранным товарам:
# - Популярность нововведения. Посчитайте, сколько товаров было добавлено в избранное.
# - Количество звёздочек для каждого товара. То есть, сколько раз товар был добавлен в избранное для каждого из товаров.
# Для того, чтобы различать товары используйте идентификатор в поле item_id — он уникален для каждого товара.
# По сути, вам надо рассчитать в программе количество звёздочек для каждого такого идентификатора.


# Вопрос 1. Сколькими браузерами пользуются наши клиенты?
# Вопрос 2. Какова общая сумма всех покупок?

# Задания
# B2.14.3 Второй журнал: браузеры
# B2.14.4 Второй журнал: сумма покупок
# B2.14.5 Второй журнал: число избранных
# B2.14.6 Число "лайков" товара
# B2.14.7 Самый популярный товар
# B2.14.8 Самый непопулярный товар

import json
import collections

filename = "data/data_3000.json"
print("Работаем с файлом: ", filename)

fp = open(filename, encoding='UTF-8')
logfile_lines = fp.readlines()
fp.close()

# print(logfile_lines[0:2])
# event = json.loads(logfile_lines[0])
# print(event)

# получим список словарей из строк файла
events_list = []
for line in logfile_lines:
    event = json.loads(line)  # десереализуем строку файла в словарь
    events_list.append(event)

# print(events_list[0:2])

user_agent_name_counter = collections.Counter()  # словарь для уникальных userAgentName
item_id_counter = collections.Counter()  # словарь для уникальных товаров (item_id)
item_id_favorite_counter = collections.Counter()  # словарь для уникальных товаров (item_id), которые хоть раз были добавлены в избранное
item_price_sum = 0

# Расчет показателей
# Условие 1. Для расчета всех перечисленных показателей необходимо брать только уникальные —
# поле detectedDuplicate ложно
# и неиспорченные — поле detectedCorruption ложно — записи.
# Условие 2. Сумму значений поля item_price, для тех событий, у которых поле eventType равно itemBuyEvent

for event in events_list:
    if not event['detectedDuplicate'] and not event['detectedCorruption']:
        user_agent_name_counter[event['userAgentName']] += 1  # считаем количество вхождений для каждого userAgentName
        if event['eventType'] == 'itemBuyEvent':
            item_price_sum += event['item_price']  # считаем общую сумму покупок
        item_id_counter[event['item_id']] += 1  # считаем количество вхождений товаров
        if event['eventType'] == 'itemFavEvent':
            item_id_favorite_counter[event['item_id']] += 1  # считаем количество вхождений товаров, которые были добавлены в избранное

# список топ браузеров по использованию
print("\nСписок ТОП наиболее используемых агентов")
for agent, cnt in user_agent_name_counter.most_common(5):
    print("{} -- {}".format(agent, cnt))

# число различных браузеров среди всех клиентов
# количество уникальных агентов (браузеров)
user_agent_name_quantity = len(user_agent_name_counter)
print("\nКоличество уникальных userAgentName: ", user_agent_name_quantity)

# общая сумма покупок
print("Общая сумма покупок: ", item_price_sum)

# Количество уникальных товаров и количество уникальных товаров в избранном
print("\nКоличество уникальных товаров: ", len(item_id_counter))
print("Количество уникальных товаров в избранном: ", len(item_id_favorite_counter))

# Максимальное значение и его ключ
print("Max лайков: ", max(item_id_favorite_counter.values()))
print("Ключ товара для max лайков",
      max(item_id_favorite_counter, key=item_id_favorite_counter.get))  # Ключ Get dict key by max value
# Минимальное значение и его ключ
print("Min лайков: ", min(item_id_favorite_counter.values()))
print("Ключ для min лайков", min(item_id_favorite_counter, key=item_id_favorite_counter.get))  # Ключ Get dict key by max value

# список топ товаров в избранном
print("\nСписок ТОП товаров в избранном")
for item, cnt in item_id_favorite_counter.most_common(10):
    print("{} -- {}".format(item, cnt))
