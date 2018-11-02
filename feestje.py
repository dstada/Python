"""Calculate days alive now
   Project: Feestje
   Dick Stada
   Oct. 2018
"""
import calendar
import datetime
a = int(input("Enter your birthday first enter your birth year : "))
b = int(input("Enter your month now : "))
c = int(input("Enter your day now : "))

today = datetime.date.today()
birthday = datetime.date(a, b, c)
diff = birthday - today
a = diff.days
b = -a
print("Today is your {}th day.".format(b))


from dateutil.relativedelta import *
from datetime import date
today = date.today()
dob = date(1982, 7, 5)
age = relativedelta(today, dob)
print(age)

datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
datetime.datetime(2012, 3, 23)
print(datetime.datetime.today().weekday())

print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][calendar.weekday(2017, 12, 22)])
