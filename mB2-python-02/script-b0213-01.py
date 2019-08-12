# B2.12_1 Задача подсчета частот слов в заданном тексте

import collections

FILENAME = "data/aviator.txt"

fp = open(FILENAME, encoding='UTF-8')
text_lines = fp.readlines()
fp.close()

# --- Вариант 1
# обычный словарь

counter = {}
for line in text_lines:
    words = line.split()
    for word in words:
        filtered_word = word.strip('.').strip(',').strip(')').strip('(').strip('–').lower()
        if filtered_word:
            if filtered_word not in counter:
                counter[filtered_word] = 1
            else:
                counter[filtered_word] += 1


for word, cnt in counter.items():
    print("{} -- {}".format(word, cnt))

print("-------------------------------------------------------------")

# --- Вариант 2
# collections.defaultdict(int)

counter = collections.defaultdict(int)

for line in text_lines:
    words = line.split()
    for word in words:
        filtered_word = word.strip('.').strip(',').strip(')').strip('(').strip('–').lower()
        if filtered_word:
            counter[filtered_word] += 1

for word, cnt in counter.items():
    print("{} -- {}".format(word, cnt))

print("-------------------------------------------------------------")

# --- Вариант 3
# collections.Counter()

counter = collections.Counter()

for line in text_lines:
    words = line.split()
    for word in words:
        filtered_word = word.strip('.').strip(',').strip(')').strip('(').strip('–').lower()
        if filtered_word:
            counter[filtered_word] += 1

# используем метод most_common(10)
# для вывода 10 наиболее частых слов
for word, cnt in counter.most_common(10):
    print("{} -- {}".format(word, cnt))
