"""[Challenge] Kaprekar's Constant

Number of four digits
Arrange the digits descending and ascending
Subtract and do the steps again until the result stays the same.

By Dick Stada, June, 2018
"""
# from re import match
from re import match


def find_kaprekar(n):
    old = ""
    while n != old:
        old = n
        low = ''.join(sorted(n))
        high = ''.join(reversed(low))
        n = str(int(high) - int(low))
        print("{} - {} = {}".format(high, low, n))
    return n


format = "[0-9]{3,4}"        # must be 3 or 4 digits
while True:
    new = input("Give number of three or four digits: ")
    print(new)
    if match(format, new) and int(new) > 100:
        break
    else:
        print("Wrong. Try again.")

while True:
    low = str(''.join(sorted(new)))   # sorteren van laag naar hoog
    counter = 1
    for i in range(0,len(low)-1):
        if low[i] == low[i+1]:
            counter += 1
    if len(new) // 2 >= counter:
        print("In orde.")
        break
    else:
        print("Te veel dezelfde cijfers in het getal.")

print("Kaprekar's Constant: {}".format(find_kaprekar(new)))

