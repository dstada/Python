"""A number is called a Disarium number if the sum of the powers of its digits
equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: True
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3

Bonus: Print all disarium numbers in a given range.

By: Dick Stada, NL
October 2018
"""
nmbr_from = int(input("Give the number to  start with:"))
nmbr_upto = nmbr_from
while nmbr_upto <= nmbr_from:   # nmbr_upto must be equal or greater
    nmbr_upto = int(input("Give a maximum number:"))


def check_disarium(num):
    str_nmbr = str(num)
    total = 0
    exponent = 1
    for i in str_nmbr:
        total += int(i)**exponent
        exponent += 1
    if total == num:
        return True
    return False


if __name__ == "__main__":
    disariums = 0
    for x in range(nmbr_from, nmbr_upto + 1):
        if check_disarium(x):
            print("{} is a disarium number.".format(x))
            disariums += 1
    if disariums == 0:
        print("No numbers that are a disarium number in this range.")

