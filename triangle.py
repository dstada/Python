"""Triangle

Write a program that takes three integer values from the user input and outputs true if a triangle can be constructed with the sides of given length.

For example:
Input: 3, 4, 5
Output: True

Input: 10, 2, 9
Output: True

Input: 7, 9, 1
Output: False

By: Dick STADA, NL
November 2018
"""
sides = []
for s in range(3):
    try:
        nbr = int(input("Give positive number: "))
        sides.append(nbr)
    except ValueError:
        print("Number is no integer. Run again.")
        exit()

sides_asc = sorted(sides)    # sort ascending
print(sides_asc)
if sides_asc[0] + sides_asc[1] < sides_asc[2]:
    print("Triangle can't be constructed.")
else:
    print("Triangle can be constructed.")
