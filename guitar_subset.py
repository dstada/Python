"""Guitar Subset

For a list of integers S and a target number G, a subset of S that adds up to G is called a guitar subset.

For example:
Input:
24
[12, 1, 61, 5, 9, 2]
Output:
[12, 9, 2, 1]
(G=24, S=[12, 1, 61, 5, 9, 2], there is a guitar subset [12, 9, 2, 1] that adds up to 24).

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

Write a program to check if the user input has a guitar subset for the specified number G
or not (both the list of integers and the number G are input parameters).
"""

import itertools
nmbr = int(input("Give a number:"))
lst_str = input("Give a list of integers, separated by a space")
# Make list of the numbers in lst_str:
lst = lst_str.split()       # Make a list of the input string
lst_int = []
for i in lst: lst_int.append(int(i))
# Make a list of all possible combinations of the input-list-items:
combinations = []
for i in range(1, len(lst_int) + 1):       #  1 until lenght of the list
    # Do itertools.combinations with the input list en dan  voor het aantal keer dat de inputlist lang is,
    # Number of items in the combination should be i,
    # Create a small list:
    comb = [list(x) for x in itertools.combinations(lst_int, i)]
    combinations.extend(comb)            # Extend the combinations list with the little com list

# Test is sum of each item is equal to the input number:
outpt = []
for x in combinations:
    if  sum(x) == int(nmbr):
        outpt.append(x)
if len(outpt) > 0:
    print("Possible combinations:")
    for q in outpt:
        print(q)
else:
    print("No combinations possible...")


