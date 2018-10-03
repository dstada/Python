"""
1 2 3
4 5 6
7 8 9


1   2   3   4
5   6   7   8
9  10  11  12
13 14  15  16

"""

# print(1,2,3,4, end="", flush=True)
n = 5

number_of_lists = 5
# empty_lists = [[] for i in range(number_of_lists)]

# Maak een list met aantal lists afhankelijk van input:
empty_lists = [[[] for i in range(number_of_lists)] for i in range(number_of_lists)]

empty_lists[0][0].append(1)

empty_lists[0][1].append(2)

empty_lists[0][2].append(3)

empty_lists[1][0].append(4)

empty_lists[1][1].append(5)

empty_lists[1][2].append(6)

empty_lists[2][0].append(7)

empty_lists[2][1].append(8)

empty_lists[2][2].append(9)

print(empty_lists)

if len(empty_lists[1]) == 0:
    print("leeg")
else:
    print("vol")

for x in range(0, n):
    print(empty_lists[x])

# Bepaal middelste cel:
mid_cel = empty_lists[int((n-1)/2)][int((n-1)/2)]
print(mid_cel)