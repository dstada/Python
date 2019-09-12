"""Harshad Number

A harshad number (or Niven number) is an integer that is divisible by the sum of its digits.

For example:
Input: 18
Output: true (18 is a Harshad number because it is divisible by the sum of its digits: 18 = (1 + 8) x 2)

Input: 1729
Output: true (1729 is a Harshad number because it is divisible by the sum of its digits:
1729 = (1 + 7 + 2 + 9) × 91)

Write a program to check if the user input is a Harshad number or not.

D.Stada - 12-Sep-2019
"""


def is_harshad(n):
    sum = 0
    for letter in n:
        sum += int(letter)
    if int(n) % sum == 0:
        return True
    else:
        return False

# In case of one number:
# n = input("Give a number: ")
# if is_harshad(n):
#     print("{} is a Harshad Number!".format(n))
# else:
#     print("{} is not a Harshad Number...".format(n))

# In case of a list:
first = input("Give first number: ")
last = input("Give last number: ")
# Swap if first number greater than last number:
if int(first) > int(last):
    first, last = last, first
lijst = []
for i in range(int(first), int(last)+1):
    if is_harshad(str(i)):
        lijst.append(i)
if len(lijst) == 0:
    print("No Harshad Numbers in this range...")
else:
    print("Harshad Numbers in this range: {}".format(lijst))
