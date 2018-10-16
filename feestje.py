"""Calculate days alive now
   Project: Feestje
   Dick Stada
   Oct. 2018
"""
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
