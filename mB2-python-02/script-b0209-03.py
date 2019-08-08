# B2.9 Функции

# Пользуясь полученными знаниями, напишем функцию приветствия.
# Она будет принимать на вход 2 параметра, имя и пол человека, и выводить на экран приветствие.

def greet(name, gender):
    #    """Приветствует пользователя по имени в соответствии с полом."""
    if gender == "male":
        print("Hello, Mrs. ", name)
    elif gender == "female":
        print("Hello, Miss. ", name)

greet("Jane", "female")
greet("John", "male")
greet("John Johnsson", "male")
greet("Jane Jafferson", "female")

