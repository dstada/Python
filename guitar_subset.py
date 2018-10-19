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
from itertools import combinations
nmbr = int(input("Give a number:"))
# S = []
lst_str = input("Give a list of integers, separated by a space")
print(lst_str)
# Make list of the numbers in lst_str:
lst = lst_str.split()       # Make a list of the npu string
print(lst)
# Find out all combinations of the elements of lst:


from itertools import combinations as comb
g = int(input())
l = list(input().split(","))
for i in range(len(l)):
    l[int(i)] = int(l[int(i)])
def solve():
    for i in range(len(l)):
        for c in comb(l,i+1):
            if sum(c) == g:
                yield c
if solve() == None:
    print("No subsets found.")
    exit()
print("Target number:",g,"\nInitial set:",l,"\nGuitar subset(s):",list(solve()))

if __name__ == "__main__":
    print("Einde")