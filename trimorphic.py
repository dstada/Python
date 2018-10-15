"""A Trimorphic Number is a number whose cube
ends in the number itself.

For example:
Input: 4
Output: True (4^3 is 64, ends in 4)

Input: 249
Output: True (249^3 = 15438249, end with 249)
"""

nmbr = int(input("Give a number: "))

if str(nmbr ** 3)[-len(str(nmbr))::] == str(nmbr):
    print("{} is trimorphic!".format(nmbr))
else:
    print("No, sorry. {} is not trimorphic.".format(nmbr))
