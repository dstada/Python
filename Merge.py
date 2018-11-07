"""Merge Sorted Arrays

Write a program that reads two sorted arrays from the user input, merges them into the third array
and outputs the result. Arrays are sorted in ascending order. For example,
the result of merging [1, 5, 8, 9] and [2, 3, 3, 14] is [1, 2, 3, 3, 5, 8, 9, 14].

For example:
Input:
1, 2, 3, 4
1, 1, 1, 42
Output:
1, 1, 1, 1, 2, 3, 4, 42

Input:
25, 55
1, 3, 94
Output:
1, 3, 25, 55, 94
"""

arr1 = sorted(list((map(int, input("Give a row of numbers, separated by a space:").split()))))
arr2 = sorted(list((map(int, input("Give another row of numbers, separated by a space:").split()))))
arr3 = sorted(arr1 + arr2)
print(arr3)
