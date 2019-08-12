# B2.12 Разделение и объединение строк

# Вооружившись методом join, допишите следующую функцию:

# Функция принимает на вход абзац текста text в виде строки и возвращает строки полученного абзаца,
# разделенные HTML тегом <BR>.

def html_line_breaks(text):
    sentences = text.split("\n")
    print(sentences)
    result = "<BR>".join(sentences)
    return result

string = html_line_breaks("Функция \n"
                          "принимает на вход абзац текста text \n"
                          "в виде строки и возвращает строки полученного абзаца \n")
print(string)