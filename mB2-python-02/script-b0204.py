file_object = open("input.txt")
file_content = file_object.read()

# Распечатаем на экран переменную file_content:
print(file_content)

print ("------------------")

file_object = open("input.txt")
line_number = 0
for line in file_object:
    line_number += 1
    print(line_number)
    print(line)
