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
    first_nmbr = input("Enter first number: ")
    if match(pattern, first_nmbr):
        break
    else:
        print("No number. Please try again.")
while True:
    last_nmbr = input("Enter last number: ")
    if match(pattern, last_nmbr) and int(last_nmbr) > int(first_nmbr):
        break
    else:
        print("Wrong. Try again.")

print("Armstrong numbers in the range from {0} to {1}: ".format(first_nmbr, last_nmbr))

nmbr_list = []


def check_armstrong(number):
    exponent = len(str(number))
    sum = 0
    for n in str(number):
        sum += int(n)**exponent
    if sum == number:
        nmbr_list.append(number)


for i in range(int(first_nmbr), int(last_nmbr)+1):
    check_armstrong(i)

if len(nmbr_list) == 0:
    print("No numbers found.")
else:
    for x in nmbr_list:
        print(x)

