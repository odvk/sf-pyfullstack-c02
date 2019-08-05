# В1.12 Интерполяция строковых переменных

unread_emails = 5
message_template = "Непрочитанных писем: "

print(message_template, unread_emails)
print("---------")


beginning = "У вас"
ending = "непрочитанных писем."
print(beginning, unread_emails, ending)
print("---------")

print(beginning + " " + str(unread_emails) + " " + ending)
print("---------")

#Классическая вставка (или вставка в printf-стиле)
print("#Классическая вставка (или вставка в printf-стиле)")

message_template = "У вас %s непрочитанных писем."
print(message_template % unread_emails)
print("---------")

long_template = """Привет! У вас %s непрочитанных писем,
%s несъеденных леденцов,
и вас ждут %s маленьких котиков."""
print(long_template % (unread_emails, 6, 7))
print("---------")

poetry_template = """%(action)s, %(action)s, %(actor)s
How I wonder what you're at!
Up above the world you fly,
Like a tea tray in the sky.
%(action)s, %(action)s, %(actor)s
How I wonder what you're at."""

print(poetry_template % {"action": "twinkle", "actor": "little bat"})
print("---------")

#Вставка через .format()
print("#Вставка через .format()")

print("The sum is {}".format(2+2))
print("---------")
print("Hello {name}! How are you doing today, {name}?".format(name="Mr. Potter"))
print("---------")

email_template = """Hello, {name}!
Congratulations! Starting now, your {product} Trial unlocks amazing video and entertainment benefits. Here are just a few of the many TV shows included with your membership:
— {prime_show}
— {second_prime_show}
— {family_show}

Thanks again for joining us!"""
print(email_template.format(name="Knight", product="Knightflix", prime_show="Eggs Today", second_prime_show="Foo walks into a Bar", family_show="C++ for babies"))
print("---------")

