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

# len_nmbrs = len(nmbrs)
# print(len_nmbrs)
# for i in range(len_nmbrs-1):
#     arr_temp = []

nmbrs.append([1,2])
print(nmbrs)

print(nmbrs[1])
print(nmbrs[0])
