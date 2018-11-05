"""
Enter your phone number and it will convert it into phone number format.
"""
num = input("Your Phone No.:\n")
print(f'({num[:3]}){num[3:6]}-{num[6:]}')