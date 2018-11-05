"""Telephone Number

Write a program that converts an integer input to a telephone number format.

Input: 1234567890  Output: (123)456-7890

Input: 37465498721  Output: (+374)65-498-721

By: Dick STADA, NL
November 2018
"""

nbr = "abc"
# Phone number cannot be empty or be characters or less than 10 or more then 15 positions:
while nbr == "" or not nbr.isdigit() or len(nbr) > 15 or len(nbr) < 10:
    nbr = input("Your phone number: ")

if len(nbr) > 11:
    print("(", nbr[:3], ")", nbr[3:6], "-", nbr[6:9], "-", nbr[9:len(nbr)], sep="")  # separator needed to avoid spaces
else:
    print("(", nbr[:3], ")", nbr[3:6], "-", nbr[6:len(nbr)], sep="")  # separator needed to avoid spaces




