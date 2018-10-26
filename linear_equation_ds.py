"""Linear Equation Solver

A linear equation is an equation that may be put in the form a * x + b = c, where x is the variable, a, b, c are
the coefficients, which are often real numbers.
The solution of such an equation is the value that, when substituted to the unknown (the x), make the equality true.

For example:
Input: "2x - 3 = 1"
Output: "x = 2"

Input: "3 = 1 + 2x"
Output: "x = 1"

Write a program that reads a linear equation as a string from the user input, solves and outputs the solution.

By: Dick STADA, NL
October 2018
"""


def calculate_x(eq_input):
    # eq_input = input("Type the equation (like -12.5x + 34.7 = 234 of 3 = 1 + 2x): ")
    eq = eq_input.lower().replace(" ", "")    # No spaces, lower case

    # Split the equation at the equal sign and find out which part has the x:
    if eq.split("=")[0].find("x") >= 0:
        eq_x_side = eq.split("=")[0]
        eq_non_x_side = eq.split("=")[1]
    else:
        eq_x_side = eq.split("=")[1]
        eq_non_x_side = eq.split("=")[0]

    # Find out the elements in the x-side of the equation:
    if len(eq_x_side.split("x")[1]) > 0:    # if there is something right of x, x-part is left
        rest_value_x_part = eq_x_side.split("x")[1]  # x in left part; part after x is rest value
        x_part_value = eq_x_side.split("x")[0]
    else:                                   # nothing right of x, so x-part is right part
        # Utter right sign plus or minus:
        if eq_x_side.split("x")[0].rfind("+") > eq_x_side.split("x")[0].rfind("-"):
            split_sign = "+"
        else:
            split_sign = "-"
        rest_value_x_part = eq_x_side.split(split_sign)[0].split("-")[0]
        x_part_value = eq_x_side.split("x")[0].split(split_sign)[1]

    # Calculate x:
    x = (float(eq_non_x_side) - float(rest_value_x_part)) / float(x_part_value)
    print("{} --> x = {}".format(eq_input, x))


if __name__ == "__main__":
    calculate_x(input("Type the equation (like -12.5x + 34.7 = 234 of 3 = 1 + 2x): "))
