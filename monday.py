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
November 2018
"""
import datetime
from dateutil import parser

print("Give your day and choose your format.")
dt = input("Step 1: Give date: ")
cmd = None
while cmd != 'x':
    print("Step 2: choose your date format a - h")
    cmd = input('[a] 21/03/2012 \n[b] January 11, 2010\n[c] 11 january 2018\n[d] 2012, 3, 23 \n[e] 20181231\n'
                '[f] 31122018\n[g] 31-12-2018\n[h] 12-31-2018\nE[x]it\n')
    cmd = cmd.lower().strip()
    try:
        if cmd == 'a':
            day, month, year = (int(x) for x in dt.split('/'))
            break
        elif cmd == 'b' or cmd == 'c':
            print(parser.parse(dt).strftime("%A"))
            break
        elif cmd == 'd':
            year, month, day = (int(x) for x in dt.split(','))
            break
        elif cmd == "e":    # 20181231
            year = int(dt[:4])
            month = int(dt[4:6])
            day = int(dt[6:])
            break
        elif cmd == "f":    # 31122018
            year = int(dt[4:])
            month = int(dt[2:4])
            day = int(dt[0:2])
            break
        elif cmd == "g":
            day, month, year = (int(x) for x in dt.split('-'))
            break
        elif cmd == "h":
            month, day, year = (int(x) for x in dt.split('-'))
            break
        elif cmd != 'x':
            print("Sorry, we don't understand {}".format(cmd))
    except Exception:
        print("Sorry, your date is not in a known format. Try again.")
        break
if cmd in ("a", "d", "e", "f", "g", "h"):
    ans = datetime.date(year, month, day)
    print(ans.strftime("%A"))

