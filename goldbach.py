"""Goldbach's Conjecture

Goldbach's conjecture is a rule in math that states the following: every even number greater than 2
can be expressed as the som of two prime numbers.

Write a program that finds every possible pair of prime numbers, whose sum equals the given number
or a set of numbers within a range.

For example:
Input: 16
Output:
3 + 13
5 + 11

Input: 32
Output:
3 + 29
13 + 19

Input: 4, 8
Output:
4: 2 + 2
6: 3 + 3
8: 3 + 5
"""

from itertools import combinations

print("Give a range, start with a number greater than two. Both numbers may be the same")
frm = int(input("From: "))
upto = int(input("Until: "))


def prime(n):       # check if the number is a prime
    for j in range(2, int(n ** .5) + 1):
        if n % j == 0:
            return False
    return True


def goldbach(getal):
    primes = []
    # Make array of all primes from 2 until number:
    for i in range(2, getal+1):
        if prime(i):
            primes.append(i)
    paren = list(combinations(primes, 2))
    for i in range(len(paren)):
        som = paren[i][0] + paren[i][1]
        if getal % 2 == 0 and som == getal:    # check if som of the two pairs is equal with the number
            print("{}: {} + {}".format(getal, paren[i][0], paren[i][1]))
    for j in range(len(primes)):
        som = 2 * primes[j]
        if som == getal:    # check if two times the prime makes the number
            print("{}: {} + {}".format(getal, primes[j], primes[j]))


for k in range(frm, upto+1):
    goldbach(k)

