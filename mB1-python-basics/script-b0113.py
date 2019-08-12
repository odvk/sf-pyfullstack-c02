# B1.13 Вложенные конструкции
print("---------")

school_marks = {"Иванов": [5, 4, 4, 5, 5],
                "Петров": [3, 3, 4, 3, 5],
                "Курочкина": [5, 5, 5, 4, 5],
                "Тупицын": [3, 3, 3, 2, 2],
                }
print(school_marks)
print(school_marks['Иванов'][1])
print("---------")

# Посчитаем средний балл каждого студента:
mean_marks = {}
for student, marks in school_marks.items():
    mean_marks[student] = sum(marks) / len(marks)

print(mean_marks)
print("---------")

# Списки тоже могут содержать вложенные сложные объекты — мы видели,
# что список может содержать другой список, но, помимо этого, он, конечно, может содержать и словарь.

events = [
    {
        "authenticated": "antoine.dickerson",
        "url": "https://www.christywatts.com/735/201.php",
        "timestamp": "2016-12-24 16:50:08",
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "ip": "53.143.50.131",
        "res_status": 404,
        "res_size": 4129136,
    },
    {
        "authenticated": "patrice.camacho",
        "url": "http://www.austinwalker.com/981.png",
        "timestamp": "2016-12-24 16:50:08",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
        "ip": "48.26.166.195",
        "res_status": 200,
        "res_size": 590813,
    },
    {
        "authenticated": "maurice.francis",
        "url": "https://www.frankie-paul.com/182.php",
        "timestamp": "2016-12-24 16:50:08",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
        "ip": "117.45.110.155",
        "res_status": 200,
        "res_size": 3103266,
    },
    {
        "authenticated": "-",
        "url": "https://www.nicolemckinney.com/631/784/669/591.html",
        "timestamp": "2016-12-24 16:50:08",
        "user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "ip": "66.220.33.180",
        "res_status": 404,
        "res_size": 1812680,
    },
    {
        "authenticated": "-",
        "url": "https://www.abbeyhickman.com/391.jpg",
        "timestamp": "2016-12-24 16:50:08",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "ip": "181.196.3.20",
        "res_status": 200,
        "res_size": 1598792,
    },
]

print(events[0])
print(events[0]["res_size"])
print("---------")

# В ключе "res_size" лежит количество байт, переданных сервером. Давайте посчитаем, сколько данных сервер отдал всего.
total_size = 0
for event in events:
    total_size = total_size + event["res_size"]

print(total_size / 1000000, "MB")
