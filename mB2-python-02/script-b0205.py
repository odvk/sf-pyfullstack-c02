file_object = open("test_file_01.txt", "w")
file_object.write("Hello, world!")
file_object.write("I know how to write this line to a file with Python")
# file_object.flush()
file_object.close()

# строки с разделителями

file_object.write("\n")
file_object.write("String 1\n")
file_object.write("String 2\n")
#file_object.flush()
file_object.close()

# Попробуем записать строку с кириллическими символами:
# Если мы планируем записывать в файл строки в отличной от ASCII кодировке,
# правилом хорошего тона считается явное указание необходимой кодировки.
# Укажем кодировку файла в специальном аргументе функции open:

file_object = open("test_file_01.txt", "w", encoding="utf-8")
file_object.write("Hello, world!\n")
file_object.write("I know how to write this line to a file with Python\n")
file_object.write("Эта строка написана на русском языке")
#file_object.flush()
file_object.close()


# После того, как работа с файлом завершена, принято его явно закрывать.
# Для этого предусмотрен специальный метод .close.
# При его вызове все содержимое накопленного буфера записывается на диск и объект файла уничтожается.
# Подчеркнем, что после вызова метода .close автоматически вызывается метод .flush,
# то есть вызывать его вручную перед закрытием файла не нужно.
# Более того, обычный сценарий работы предполагает открытие файла,
# запись в него необходимых данных и закрытие файла. Мы вызывали метод .flush вручную,
# чтобы посмотреть на промежуточный результат.