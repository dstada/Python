eq = input("Type the equation (like -12.5x + 34.7 = 234): ")
eq = eq.lower().replace(" ", "")
print(eq)

# Split the equation on the equal sign:
eq_left = eq.split("=")[0]
eq_right = eq.split("=")[1]
print("Links: {} and right: {}".format(eq_left, eq_right))

# Split the part with the x (aangenomen dat x altijd in links zit):
eq_left_left = float(eq_left.split("x")[0])
print(eq_left_left)

# https://code.sololearn.com/cZJeTyhTIexH/#py