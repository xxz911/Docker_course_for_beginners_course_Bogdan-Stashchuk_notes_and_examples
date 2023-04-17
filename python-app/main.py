import calendar

print("Добро пожаловать в календарь\n")

year = int(input("Введите год: "))
month = int(input("Введите номер(1-12) месяца: "))

print(calendar.month(year, month))

print("Всего хорошего!")
