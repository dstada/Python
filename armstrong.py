"""Armstrong Numbers

Check if a number is an armstrong number
(sum of the cubes of the digits equal to the number itself)

Print al armstrong numbers in a given range.

Made by Dick Stada, the Netherlands, May 31st, 2018
"""
from re import match

# Input check with regular expression:
pattern = "^[0-9]+$"
while True:
    nmbr = input("Enter a number: ")
    if match(pattern, nmbr):
        break
    else:
        print("No number. Please try again.")


def check_armstrong(number):
    exponent = len(number)
    sum = 0
    for n in number:
        sum += int(n)**exponent
    if sum == int(number):
        print("{} is an armstrong number!".format(number))
    else:
        print("{} is not an armstrong number.".format(number))


check_armstrong(nmbr)


while True:
    new = input("Give number of three or four digits: ")
    print(new)
    if match(format, new) and int(new) > 100:
        break
    else:
        print("Wrong. Try again.")


