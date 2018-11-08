"""Gapful Numbers

A gapful number is a number of at least 3 digits that is divisible by the number formed by the first
and last digit of the original number.

Input: 192  Output: true (192 is gapful because it is divisible 12)

Input: 583  Output: true (583 is gapful because it is divisible by 53)

Input: 210  Output: false (210 is not gapful because it is not divisible by 20)

Write a program to check if the user input is a gapful number or not.

Bonus: Print all the gapful numbers in a given range.

---------------Important-----------------------
If you want a range, enter the lower and the upper bound separated by a space.
example:
100 200

If you just want to check for a number, just input your number.
example:
120
-------
By: Dick Stada, NL
November 2018

"""


def gap_check(nbr):
    if int(nbr) % int(nbr[:1] + nbr[len(nbr)-1:]) == 0:
        print("{} is a gapful number!".format(nbr))
    else:
        print("{} is not a gapful number...".format(nbr))


# number(s) should be > 99 and max two numbers. Lowest and highest automatically ordered:
arr_n = ["99"]
try:
    while int(arr_n[0]) < 100 or len(arr_n) > 2:
        arr_n = sorted(list(input("Enter a number > 99. If you want a range, give lowest and highest "
                            "with a space in between:").split()))
except:
    print("Something gone wrong. Please try again.")
    exit()


if len(arr_n) > 1:
    for n in range(int(arr_n[0]), int(arr_n[1]) + 1):
        gap_check(str(n))
else:
    gap_check(arr_n[0])
