import math
from re import match

# check input
format = "^[^,\D]*,[^,\D]*$"        # must be two numbers separated by a comma
while True:
    coordA = input("Give x and y of the FIRST point, separated by a comma: ")
    print(coordA)
    if match(format, coordA):
        break
    else:
        print("Wrong. Try again.")

while True:
    coordB = input("Give x and y of the SECOND point, separated by a comma: ")
    print(coordB)
    if match(format, coordB):
        break
    else:
        print("Type two numbers, separated by a comma. Try again please.")

xA = int(coordA.split(",")[0])
xB = int(coordB.split(",")[0])
yA = int(coordA.split(",")[1])
yB = int(coordB.split(",")[1])
dist = round((math.sqrt((yB - yA)**2 + (xB - xA)**2)), 2)
print("The distance between ({}) and ({}) is {}.".format(coordA, coordB, dist))




