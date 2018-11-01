"""Monday

Write a program that finds the day of the week from a given date in a string. Support as many date formats as possible.

For example:
Input: "Oct 30, 2018"
Output: "Tuesday"

Input: "2017-11-5"
Output: "Sunday"
0 nieuw
Ongelezen

By: Dick STADA
October 2018
"""
import datetime
import calendar
from dateutil import parser

datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
datetime.datetime(2012, 3, 23)
print(datetime.datetime.today().weekday())

# ================================================
dt = '21/03/2012'
day, month, year = (int(x) for x in dt.split('/'))
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))
# ================================================

print("start")
print(parser.parse('January 11, 2010').strftime("%A"))
print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][calendar.weekday(2017, 12, 22)])
print("einde")


print("===========================================")
print("Give your day and choose your format:")
dt = input("Give date: ")
cmd = None
while cmd != 'x':
    cmd = input('[a] 21/03/2012 \n[b] January 11, 2010 \n[c] 2012, 3, 23 \n[d] 20181231\n[e] 31122018\nE[x]it\n'
                '[f] 31-12-2018\n[g] 12-31-2018')
    cmd = cmd.lower().strip()
    if cmd == 'a':
        day, month, year = (int(x) for x in dt.split('/'))
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd == 'b':
        print("Choice is b")
        form = "b"
        break
    elif cmd == 'c':
        year, day, month = (int(x) for x in dt.split(','))
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd == "d":    # 20181231
        year = int(dt[:4])
        print(year)
        month = int(dt[4:6])
        print(month)
        day = int(dt[6:])
        print(day)
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd == "e":    # 31122018
        year = int(dt[4:])
        print(year)
        month = int(dt[2:4])
        print(month)
        day = int(dt[0:2])
        print(day)
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd == "f":
        day, month, year = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd == "g":
        month, day, year = (int(x) for x in dt.split('-'))
        ans = datetime.date(year, month, day)
        print(ans.strftime("%A"))
        break
    elif cmd != 'x':
        print("Sorry, we don't understand {}".format(cmd))
