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

eq = input("Type the equation (like -12.5x + 34.7 = 234): ")
eq = eq.lower().replace(" ", "")    # No spaces, lower case


# Split the equation at the equal sign:
eq_left = eq.split("=")[0]
eq_right = eq.split("=")[1]
# Find out the part with x:
if eq_left.find("x"):
    eq_left_x = eq_left     # left part has an x
else:
    eq_right_x = eq_right   # right part has an x

if 'eq_left_x' in globals():
    print("ja")
else:



print("Links: {} and right: {}".format(eq_left, eq_right))
# Find out at what side the x is:
if eq_left.find("x"):
    print("Hier zit x in!")
    # Bepalen waar x staat:
    if float(eq_left.split("x")[1]) > 0:
        print("x zit in rechterdeel")
    else:
        print("x zit in linkerdeel")



# Split the part with the x (aangenomen dat x altijd in links zit):
eq_left_left = float(eq_left.split("x")[0])
print(eq_left_left)
eq_left_right = float(eq_left.split("x")[1])
print(eq_left_right)
# Left number to the right:
eq_right = eq_right - eq_left_right
print(eq_right)
# Get x by dividing right by left:
eq_right = eq_right / eq_left_left
print("x = {}".format(eq_right))

# https://code.sololearn.com/cZJeTyhTIexH/#py