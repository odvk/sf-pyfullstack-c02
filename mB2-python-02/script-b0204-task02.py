# Задание 2

# Допишите следующий фрагмент кода, который выводит на экран строки с четным номером.

FILENAME = "test_file.txt"
file_object = open(FILENAME)

lines = file_object.readlines()
print(lines)
line_index = 0
for line in lines:
    line_index += 1
    if line_index % 2 == 0:
        # выводим на экран строку line
        print(line)
