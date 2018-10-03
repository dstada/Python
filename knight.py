from re import match

pattern = "^[a-h][1-8]$"
while True:
    position = input("Enter a position. Like a3 or h8: ")
    print(position)
    if match(pattern, position):
        break
    else:
        print("Not possible. Try again please.")

hor = ("a", "b", "c", "d", "e", "f", "g", "h")
vert = (1, 2, 3, 4, 5, 6, 7, 8)
hor_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# Possibilities:
# print("Horizontaal: {} en verticaal: {}".format(position[0], position[1]))
#
# print("Horizontaal: {}".format(position[0]))

# if (hor_dict[position[0]] + 2) in vert:     # Komt de positie voor die horizontaal 2 posities naar rechts is?
#     print("Yes, 2 naar rechts, deze horizontale positie bestaat!")
# else:
#     print("no, deze horizon. 2 naar rechts, positie bestaat niet!")
#
# if int(position[1]) in vert:
#     print("In orde, deze verticale positie komt voor!")
# else:
#     print("Helaas, deze verticale positie valt buiten het bord.")

possibs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]      # list of tuples

for tup in possibs:
    print("Horizontaal {} en verticaal {}".format(tup[0], tup[1]))
    # check horizontal position:
    if (hor_dict[position[0]] + tup[0]) in vert:
        print("Ja!!!!")
    else:
        print("Nee!!!")
    # check vertica position:
    if int(position[1]) + tup[1] in vert:
        print("Ja!!!!")
    else:
        print("Nee!!!")

# if (hor_dict["a"] - 5) in vert:
#     print("Yes")
# else:
#     print("No")
#


# k = 9
# if k in vert:
#     print("Check")
# else:
#     print("No")

# pos1 = position
# pos2 =
# pos3 =
# pos4 =
# pos5 =
# pos6 =
# pos7 =
# pos8 =
