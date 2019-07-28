# B1.11 Словари

# Допустим, у нас есть словарь, где ключами выступают имена, а значениями — количество букв в них.
# Как надо дополнить код, чтобы имена вывелись отсортированными по алфавиту?

names_len = {}
people = ["Bob", "Liza", "Anna", "Fanny", "Violet"]
for person in people:
    names_len[person] = len(person)

print(names_len)

print(names_len.keys())

# код ответа  ниже
keys_ = list(names_len.keys())
keys_.sort()
print(keys_)
