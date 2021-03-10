import datetime
import time
a = input("Введите дату ГГГГ ММ ДД  ")
a = datetime.datetime.strptime(a, "%Y %m %d").strftime("%Y %m %d")
n = int(input("Введите дельту"))
print(a)
