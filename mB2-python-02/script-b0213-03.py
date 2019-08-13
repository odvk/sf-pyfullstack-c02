# B2.13 Пишем парсер логов

# Перед аналитиками веб-ресурсов постоянно встают вопросы, для ответа на которые требуется всевозможная статистика
# по аудитории ресурса. Поэтому задачи формирования аудиторной статистики являются важной и неотъемлемой частью
# ответственности любой команды разработки. Яндекс.Метрика и Google Analytics -
# примеры популярных готовых инструментов для построения подобной статистики.

# Несмотря на широкую функциональность этих инструментов, часто возникает необходимость самостоятельно
# построить какую-нибудь метрику на основании имеющихся журналов. Например, часть данных может быть недоступна
# либо их выгрузка займет слишком много времени. Другая часть данных может оказаться чувствительной
# и её нельзя отправлять в сторонние сервисы.

import collections

FILENAME = "data/dummy-access.log"

fp = open(FILENAME, encoding='UTF-8')
text_lines = fp.readlines()
fp.close()

# Вопрос 1, Вопрос 2 ----------------
# подсчитать количество запросов от ip
counter = collections.defaultdict(int)
ip = ['79.136.245.135', '127.0.0.1']

for line in text_lines:
    if ip[0] in line:
        counter[ip[0]] += 1
    if ip[1] in line:
        counter[ip[1]] += 1
print(counter)

print("-------------------------------------------------------------")

# Вопрос 3 ----------------
# Каково максимальное количество запросов от одного клиента? Введите число запросов:
counter_ip = collections.Counter()

for line in text_lines:
    words = line.split()
    #    print(words)
    #    print(words[0])
    counter_ip[words[0]] += 1

# используем метод most_common(10)
# для вывода 10 наиболее частых слов
for ip, cnt in counter_ip.most_common(10):
    print("{} -- {}".format(ip, cnt))

average_requests_qty = sum(counter_ip.values()) / len(counter_ip.values())
print("Среднее количество запросов от ip: ", round(average_requests_qty, 2))

# Максимальное значение и его ключ
print("Max запросов: ", max(counter_ip.values()))
print("Ключ для max запросов", max(counter_ip, key=counter_ip.get))  # Ключ Get dict key by max value

# Минимальное значение и его ключ
print("Min запросов: ", min(counter_ip.values()))
print("Ключ для min запросов (первый)", min(counter_ip, key=counter_ip.get))  # Ключ Get dict key by max value
