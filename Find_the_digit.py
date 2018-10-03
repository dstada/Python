"""Find the digit

Find all integers between 0 and n, which contain the digit d (is from 0 to 9)

Input: n = 20, d = 5
Output: 5, 15

Dick Stada, juli 2018
"""

n = input("Between 0 and: ")
d = input("Digit: ")

# In case d is one position:
# for i in range(int(n)+1):
#     char_i = str(i)
#     for j in char_i:
#         if j == str(d):
#             print(i)

# In case d may be several digits:
for k in range(int(n) + 1):
    if d in str(k):
        print(k)

