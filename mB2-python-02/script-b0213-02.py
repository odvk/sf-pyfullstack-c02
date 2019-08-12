# B2.12_1 Задача подсчета частот слов в заданном тексте
# Делаем реализацию скрипта script-b0213-01 через функцию

import sys
# sys.agv[1] # - путь к файлу, который укажем через пробел при запуске скрипта из командной строки
# пример: python script.py text_file.txt
# sys.agv[0] # - путь к модулю, который мы запускаем

import collections

FILENAME = "data/aviator.txt"

def main(filename):
    fp = open(filename, encoding='UTF-8')
    text_lines = fp.readlines()
    fp.close()

    counter = collections.Counter()

    for line in text_lines:
        words = line.split()
        for word in words:
            filtered_word = word.strip('.').strip(',').strip(')').strip('(').strip('–').lower()
            if filtered_word:
                counter[filtered_word] += 1
    return counter


# проверка того, что модуль не импортируется другим модулем, а запускается интерпретатором
if __name__ == '__main__':
    counter = main(FILENAME)
    for word, cnt in counter.most_common(10):
        print("{} -- {}".format(word, cnt))
