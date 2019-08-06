# B2.5 Запись в файлы
# Прочитать содержимое файла input.txt и записать его в файл output.txt в верхнем регистре.
# Действовать будем так:
# построчно читаем содержимое файла input.txt;
# приводим очередную строку к верхнему регистру, используя метод upper();
# записываем полученную строку в файл output.txt.

INPUT_FILENAME = "input01.txt"
OUTPUT_FILENAME = "output.txt"

reader = open("input01.txt")
writer = open("output.txt", "w")

for line in reader:
    transformed_line = line.upper()
    writer.write(transformed_line)

reader.close()
writer.close()
