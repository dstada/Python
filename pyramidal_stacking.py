"""Pyramidal stacking Challenge
Monday Blue Challenge Series #8

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

"""
nmbrs = [[1,2,3]]
# nmbrs = [1,2]
# nmbrs = [0,1,0,1]

len_first_row = len(nmbrs[0])
print(len_first_row)
for i in range(len_first_row-1):    # Dit moest net zoveel keer totdat er een overblijft.
    arr_temp = []
    # Pak laatste element uit nmbrs:
    print(reversed(nmbrs)))[0])

nmbrs.append([1,2])
print(nmbrs)

# print the pyramid:
for x in reversed(nmbrs):
    print(x)
