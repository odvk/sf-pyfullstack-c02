# B2.5 Запись в файлы
# Записать строку в текстовый файл можно, в том числе, используя уже знакомую нам функцию print.

file_object = open("test_file_02.txt", "w")
print("Write me to the file", file=file_object)
file_object.close()
