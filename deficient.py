"""Deficient Numbers

A number is considered deficient if the sum of its factors is less than twice that number.

For Example:
10 is a deficient number.
Factors of 10 are 1, 2, 5, 10
Sum is 1 + 2 + 5 + 10 = 18 < 2 * 10

Tasks:
(Easy) Write a program to verify whether a given number is deficient or not.
(Medium) Write a program to find all the deficient numbers in a range.
(Hard) Given a number, write a program to display its factors, their sum and then verify whether it's deficient or not.

Coded by: Dick Stada, July 2018
"""

lowest = int(input("From: "))
highest = int(input("up to: "))


def determine_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors


def deficient(lijst, num):
    if sum(lijst) < 2 * num:
        print("{} is deficient".format(num))
    else:
        print("{} is NOT deficient".format(num))
    print("The sum of the factors of {} is {}.".format(num, sum(lijst)))


for j in range(lowest, highest+1):
    # num = j
    fac_list = determine_factors(j)
    print("Factors of {}: {}".format(j, fac_list))
    deficient(fac_list, j)



