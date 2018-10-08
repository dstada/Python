"""A number is called a Disarium number if the sum of the powers of its digits
equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: True
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3

By: Dick Stada, NL
October 2018
"""

nmbr = int(input("Give a number:"))


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
    for x in range(0, nmbr+1):
        if check_disarium(x):
            print("{} is a disarium number.".format(x))
