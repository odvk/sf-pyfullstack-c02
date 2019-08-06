# B2.5 Запись в файлы
# Вставьте пропуски в программу, которая читает файл input.txt, исключает из него пустые строки,
# записывает результат в файл output.txt и после этого выводит на экран количество записанных строк.
#
# Тут мы будем использовать строковый метод strip(), который возвращает копию исходной строки без
# лишних пробелов и символов переноса строки в начале и конце строки.


FILENAME = "input02.txt"

reader = open(FILENAME)
lines = reader.readlines()
reader.close()

writer = open("output02.txt", "w")
lines_counter = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line:
        writer.write(stripped_line)
        writer.write("\n")
        lines_counter += 1

writer.close()
print(lines_counter)
