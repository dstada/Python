"""Minimal Pairs Product Sum

Write a function that receives an array of integers and returns the minimal sum of the array (sum of products of each two adjacent numbers).

For Example:
Without sorting the array [40,25,10,5,1], the sum is:
(40*25) + (25*10) + (10*5) + (5*1) = 1305

The challenge is to find the best possible sort of the array elements, to have the minimal sum result.

The expected output for the array [40,25,10,5,1]  is 225.
'''

By: Dick Stada, NL
June, 2018

"""

list_orig = [40, 1, 25, 10, 5]
list_orig.sort()
print(list_orig)
del list_orig[-1]
print(list_orig)
del list_orig[0]
print(list_orig)

# Neem laatste en zet die in nieuwe list:
list_new = []
list_new[]
