"""Prime Strings

A String is called prime if it can't be constructed by concatenating multiple (more than one) equal strings.

For example:
"abac" is prime, but "xyxy" is not ("xyxy" = "xy" + "xy").

Implement a program which outputs whether a given string is prime.

Examples
Input: "xyxy"
Output: "not prime"

Input: "aaaa"
Output: "not prime"

Input: "hello"
Output: "prime"

By: Dick Stada, NL
June, 2018
"""

test = "abdabda"
# test = "xyxy"
# test = "aaaa"

length = len(test)
if length % 2 != 0: # Odd, so Not prime if all letters are the same:
    counter = 1
    for i in range(1, length):
        if test[0] == test[i]:
            counter += 1
    if counter == length:
        print("Not prime")
else:           # Even amount of letters
    for j in range(0, length//2):
        test_str = test[0:2]
        print(test_str)



# print("sssdaf")
#
# if test[0] in test[1:4]:
#     print("Komt voor")
#
# if test == "abd"*2:
#     print("Yes")