"""[Challenge] Kaprekar's Constant - medium level

Number of four digits
Arrange the digits descending and ascending
Subtract and repeat this until the result stays the same.

Input: 101-9999, no repetitions for 3-digit numbers,
       max 2 repetitions in 4-digit numbers.

By Dick Stada - NL, June, 2018
"""

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
#    if match(format, new) and int(new) > 100:  # input of 5 digits allowed! Why??
    if match(format, new) and (100 < int(new) < 10000):
        low = str(''.join(sorted(new)))
        counter = 1
        for i in range(0, len(low) - 1):
            if low[i] == low[i + 1]:
                counter += 1
        if len(new) // 2 >= counter:
            break
        else:
            if len(new) == 3:
                print("No equal digits in a 3-digit number, please.")
            else:
                print("Only 2 digits may be the same in a 4-digit number.")
    else:
        print("Wrong input. Try again.")


print("Kaprekar's Constant: {}".format(find_kaprekar(new)))

