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

# Вопрос 1. Сколькими браузерами пользуются наши клиенты?
# Вопрос 2. Какова общая сумма всех покупок?

# Задания
# B2.14.1 Первый журнал: браузеры
# B2.14.2 Первый журнал: сумма покупок


import json
import collections

filename = "data/data_500.json"
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
item_price_sum = 0

# Расчет показателей
# Условие 1. Для расчета всех перечисленных показателей необходимо брать только уникальные —
# поле detectedDuplicate ложно
# и неиспорченные — поле detectedCorruption ложно — записи.
# Условие 2. Сумму значений поля item_price, для тех событий, у которых поле eventType равно itemBuyEvent

for event in events_list:
    if not event['detectedDuplicate'] and not event['detectedCorruption']:
        if event['userAgentName']:
            user_agent_name_counter[event['userAgentName']] += 1
        if event['item_price'] and event['eventType'] == 'itemBuyEvent':
            item_price_sum += float(event['item_price'])

# список топ браузеров по использованию
print("\nСписок ТОП наиболее используемых агентов:")
for agent, cnt in user_agent_name_counter.most_common(5):
    print("{} -- {}".format(agent, cnt))

# число различных браузеров среди всех клиентов
# количество уникальных агентов (браузеров)
user_agent_name_quantity = len(user_agent_name_counter)
print("\nКоличество уникальных userAgentName: ", user_agent_name_quantity)

# общая сумма покупок
print("Общая сумма покупок: ", item_price_sum)