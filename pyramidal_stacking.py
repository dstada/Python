"""Pyramidal stacking Challenge
Monday Blues Challenge Series #8
Let's try to build a number triangle this week! This challenge was inspired by Pascal's triangle but we will work from bottom-to-top instead of top-to-bottom this time.
TASK
Write a program to accept a list of unit digits and stack it in a triangular form. Each successive layer on top was derived from the sum of two adjacent numbers from the lower level.
EXAMPLE
[ 1, 2 ] ➡
  3
1   2

[ 1, 2, 3 ] ➡
    8
  3   5
1   2   3

[ 0, 1, 0, 1 ] ➡
       4
     2  2
   1   1   1
0   1   0   1
EXTRA
Determine the final number on the apex without building the triangle.

By: Dick STADA, Oct. 2018
"""
#nmbrs = [[1, 2]]
#nmbrs = [[1, 2, 3]]
nmbrs = [[0, 1, 0, 11]]
#nmbrs = [[1, 2, 3]]

# Create the list with the lines to print:
len_first_row = len(nmbrs[0])
for i in range(len_first_row-1):
    arr_temp = []
    rev_list = list(reversed(nmbrs))[0]

    for q in range(len(rev_list)-1):
        arr_temp.append(rev_list[q] + rev_list[q + 1])
    nmbrs.append(arr_temp)

# Building the pyramid:
space_counter = len(nmbrs) - 1
for x in reversed(nmbrs):
    print(" "*space_counter, end="")
    for y in x:
        print(y, end=' ')
    space_counter -= 1
    print()


