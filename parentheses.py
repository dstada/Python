"""Balanced Parenthesis

Create a program that checks if in a given string expression all the parenthesis are balanced.
For Example:
(test) - valid
(no() - invalid
()(()) - valid
(123(456)(7))( - invalid
(val()id) - valid

Also, take into account the "\" escape sequences:
(nope\) - invalid
(v\(al) - valid
"""

str = input("Give your text: ")
str = str.replace("\(", "").replace("\)", "").replace("\[", "").replace("\]", "").replace("\{", "").replace("\}", "")
print(str)
if str.count("}") != str.count("{") or str.count("(") != str.count(")") or str.count("[") != str.count("]"):
    print("invalid")
else:
    print("valid")

"""Below my first try:
"""
# test_string = input("Give your text: ")
# left_par = 0
# right_par = 0
# flag = 0
# print(test_string.count("("))
# for i in test_string:
#     if flag != 1:     # No flag, so check character:
#         if i != "\\":   # No escape, do check for parenthesis:
#             if i == "(":
#                 left_par += 1
#             elif i == ")":
#                 right_par += 1
#             flag = 0    # No escape, so flag on 0
#         else:           # Escape. so flag on 1 and no check:
#             flag = 1
# if left_par == right_par:   # left and right parentheses equal
#     print("valid")
# else:
#     print("invalid")
