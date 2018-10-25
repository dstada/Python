"""Linear Equation Solver

A linear equation is an equation that may be put in the form a * x + b = c, where x is the variable, a, b, c are the coefficients, which are often real numbers.

The solution of such an equation is the value that, when substituted to the unknown (the x), make the equality true.

For example:
Input: "2x - 3 = 1"
Output: "x = 2"

Input: "3 = 1 + 2x"
Output: "x = 1"

Write a program that reads a linear equation as a string from the user input, solves and outputs the solution.
"""

eq = input("Type the equation (like -12.5x + 34.7 = 234 of 3 = 1 + 2x): ")
eq = eq.lower().replace(" ", "")    # No spaces, lower case

# Split the equation at the equal sign and find out which part has the x:
if eq.split("=")[0].find("x") >= 0:
    eq_x_part = eq.split("=")[0]
    eq_non_x_part = eq.split("=")[1]
else:
    eq_x_part = eq.split("=")[1]
    eq_non_x_part = eq.split("=")[0]
print("eq_x_part: {}, eq_non_x_part: {}".format(eq_x_part, eq_non_x_part))

print("We gaan nu {} onderzoeken.".format(eq_x_part))
# Find out the elements in the x-part:
if len(eq_x_part.split("x")[1]) > 0:    # if there is something at right of x, then x-part is left
    print("x in left part")
    # x in left part; part after x is rest value
    rest_value_x_part = eq_x_part.split("x")[1]
    print("Restwaarde x-part: {}".format(rest_value_x_part))
    x_part_value = eq_x_part.split("x")[0]
    print("x value: {}".format(x_part_value))
else:                                   # nothing right of x, so x-part is right part
    print("x in right part of {}".format(eq_x_part))     # x-part has all chars right, including utter right + or - sign

    print("te bekijken deel (zonder x): {}".format(eq_x_part.split("x")[0]))   # part without x
    print("te bekijken deel (met x): {}".format(eq_x_part))
    # Min-teken erin?:
    if eq_x_part.split("x")[0].rfind("+") > eq_x_part.split("x")[0].rfind("-"):
        print("splitsteken is een +")
        split_sign = "+"
    else:
        print("splitsteken is een -")
        split_sign = "-"
    rest_value_x_part = eq_x_part.split(split_sign)[0].split("-")[0]
    x_part_value = eq_x_part.split("x")[0].split(split_sign)[1]

print("rest_value_x_part: {}".format(rest_value_x_part))
print("x_part_value: {}".format(x_part_value))

# if 'eq_left_x' in globals():
#     print("ja")
# else:
#     pass


# print("Links: {} and right: {}".format(eq_left, eq_right))
# # Find out at what side the x is:
# if eq_left.find("x"):
#     print("Hier zit x in!")
#     # Bepalen waar x staat:
#     if float(eq_left.split("x")[1]) > 0:
#         print("x zit in rechterdeel")
#     else:
#         print("x zit in linkerdeel")
#


# Split the part with the x (aangenomen dat x altijd in links zit):
# eq_left_left = float(eq_left.split("x")[0])
# print(eq_left_left)
# eq_left_right = float(eq_left.split("x")[1])
# print(eq_left_right)
# # Left number to the right:
# eq_right = eq_right - eq_left_right
# print(eq_right)
# # Get x by dividing right by left:
# eq_right = eq_right / eq_left_left
# print("x = {}".format(eq_right))

# https://code.sololearn.com/cZJeTyhTIexH/#py