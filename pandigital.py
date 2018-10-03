"""Pandigital Numbers

If a number contains each of the digits from 0 to 9 at least once (0 not being the leading digit), it is considered to be pandigital.

For example, 1076398452 is pandigital.
Similarly, 11145689723232309899 is also pandigital.

Tasks:
(Easy) Write a program to verify whether a given number is pandigital or not.
(Hard) In addition to verifying the number being pandigital, display the number of times each digit appears in that number.
"""

nbr = input("Give number which is > 0: ")
# set() gives set of unique elements
if nbr.isdigit() and int(nbr) > 0:
    if len(set(nbr)) == 10:
        print("Pandigital")
    else:
        print("NOT pandigital")

    for i in range(10):
        print("{} appears {} time(s).".format(i, nbr.count(str(i))))
else:
    print("Wrong input. Try again, please.")
