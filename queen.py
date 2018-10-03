"""
#Chess probability challenge
#Try to make a program that will give us the no. of ways to place n queens on a n*n chess board such that no queen threatens the other .
#For eg: to place 4 queens on a 4*4 chess board we have only 2 ways
#      1.    2.   3.   4.
#  1.        q
#  2.                     q
#  3. q
#  4.               q
#and other one it's reflection.

########################################################################################################################################
# Author: Lindsay Chen
# Solution:
# Since there is only one Queen allowed in each row and column, one list is enough to describe the allowed distribution
# The indexes of the list is the No. of the row on chess board, and the value of each item is the No. of the column
# e.g. [1,3,0,2] means:  In a 4X4 chess board, on row 0, the queen is placed on column 1; on row 1, the queen is placed on column 3;
#                        on row 2, the queen is placed on column 0; on row 3, the queen is placed on column 2;
# In this design, we need a function to decide if the queen is put on a diagonal with another queen, and exclude those distributions
########################################################################################################################################
"""
# Queens : fits M queens on a MxM chess board
# VcC 2018
M = 8  # Size of the grid
R = range(M)


# Code
def sl(z):
    for x in (e for e in R if e not in z):
        for y in (y for y in R if y not in z.values() and not any(x+i in z and abs(z[x+i]-y)==i or x-i in z and abs(z[x-i]-y)==i for i in range(1, max(x,y,M-x,M-y)))):
            z[x] = y
            if len(z) == M:
               return(z)
            j = sl(z)
            if j:
               return(j)
            z.pop(x)


# Test and result display
z = sl({})


print("\n".join("|".join("Q" if i in z and z[i]==j else " " for j in R) for i in R))