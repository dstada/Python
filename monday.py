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

datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
datetime.datetime(2012, 3, 23)
print(datetime.datetime.today().weekday())

dt = '21/03/2012'
day, month, year = (int(x) for x in dt.split('/'))
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))

from dateutil import parser
print(parser.parse('January 11, 2010').strftime("%A"))

print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][calendar.weekday(2017, 12, 22)])

print("Choose your format:")
cmd = None
while cmd != 'x':
    cmd = input('[a] 21/03/2012 \n[b] January 11, 2010 \n[c] 2012, 3, 23 \nE[x]it\n ')
    cmd = cmd.lower().strip()
    if cmd == 'a':
        print("Choice is a")
        break
    elif cmd == 'b':
        print("Choice is b")
    elif cmd == 'c':
        print("Choice is c")
    elif cmd != 'x':
        print("Sorry, we don't understand {}".format(cmd))

