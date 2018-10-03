"""
Tests whether a matrix is a magic square.
If it is, prints its magic number.

INPUT INSTRUCTIONS: Either just press
"Submit" or enter EACH ROW IN A NEW LINE.
Separate entries by comma and/or space.

Example 1:
1, 2, 3
4, 5, 6
7, 8, 9

Example 2:
7 12 1 14
2 13 8 11
16 3 10 5
9 6 15 4
"""

import numpy as np

def is_magic(a):
    n = a.shape[0]
    if np.unique(a).size != a.size:
        print("\nIt does not have distinct entries, so it is not a magic square :(")
        return
    d1 = sum(a[i][i] for i in range(n))
    d2 = sum(a[i][n-i-1] for i in range(n))
    if d1==d2 and np.all(a.sum(axis=0)==d1) \
    and np.all(a.sum(axis=1)==d1):
        print("\nIt is a magic square! The magic sum is", d1)
    else:
        print("\nIt is not magic square :(")

try:
    r1 = list(map(int,
    input().replace(",", " ").split()))
    d = len(r1)
    ms = np.empty([d, d], dtype = int)
    ms[0] = r1
    for r in range(1, d):
        ms[r]  = list(map(int,
        input().replace(",", " ").split()))
    print("Your matrix is:", *ms, sep="\n")
except:
    ms  = np.array([[8,1,6],
                    [3,5,7],
                    [4,9,2]])

    print("Invalid input. Working with the matrix",  *ms, sep="\n")

is_magic(ms)