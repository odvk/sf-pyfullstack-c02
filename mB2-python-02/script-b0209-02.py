# B2.9 Функции

# Функция четное/нечетное.

def tell_even(num):
    if num % 2 == 0:
        print(num, "-- чётно")
    else:
        print(num, "-- нечётно")

tell_even(2)
tell_even(5)