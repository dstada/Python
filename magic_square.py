"""
Tests whether a matrix is a magic square.
If it is, prints its magic number.

INPUT INSTRUCTIONS: Either just press
"Submit" or enter EACH ROW IN A NEW LINE.
Separate entries by comma and/or space.

Example 1:
1, 2, 3
4, 5, 6
7, 8, 9

Example 1a:
2, 7, 6
9, 5, 1
4, 3, 8

Example 2:
7 12 1 14
2 13 8 11
16 3 10 5
9 6 15 4

Example 3:
1,2,3,4
5,6,7,8
9,10,11,12
13,14,15,16

By Dick Stada, the Netherlands - 9/2018
"""
# Input first row:
while True:
    line1 = input("Give the numbers of the first line, separated by commas:")
    arr = line1.replace(",", " ").split()
    my_set = set(arr)   # my_set contains only unique numbers out of arr
    len_line = len(my_set)
    # check if the numbers are unique and number of commas is correct:
    if len_line == len(arr) and line1.count(",") == (len_line - 1):
        break   #
    else:
        print("Only unique numbers, separated by commas! Again!")
# Input rest of the rows:
for i in range(len(arr)-1):    # If there are 3 numbers in the first row, their must be 2 more rows, etc.
    while True:
        double = True
        next_line = input("Next line:")
        arr2 = next_line.replace(",", " ").split()
        my_set = set(arr2)
        # check if number of elements are the same as in the 1st line and right number of commas:
        for j in arr2:
            if j in arr:
                double = False
        if len(my_set) == len(arr2) and len(my_set) == len_line and next_line.count(",") == len_line - 1 and double:
            arr = arr + arr2
            break
        else:
            print("Numbers may not be the same or too much/less numbers! Again!")

# Convert list of strings in list of ints:
arr_int = list(map(int, arr))

hor_check = False
ver_check = False
cross_check = False
# Horizontal check:
arr_set_hor = set([sum(arr_int[x:x+len_line]) for x in range(0, len(arr_int), len_line)])
if len(arr_set_hor) == 1:
    print("Horizontal check okay!")
    hor_check = True
else:
    print("Horizontal check not okay.")

# Vertical check:
arr_ver = []
for x in range(0, len_line):
    sum = 0
    for y in range(x, len(arr_int), len_line):
        sum = sum + arr_int[y]
    arr_ver.append(sum)
if len(set(arr_ver)) == 1:
    print("Vertical check okay!")
    ver_check = True
else:
    print("Vertical check not okay.")

# Cross check:
x = 0
sum1 = 0
for x in range(x, len(arr_int), len_line+1):
    sum1 += arr_int[x]
y = 0
sum2 = 0
for y in range(len(arr_int), y, -len_line-1):
    sum2 += arr_int[y-1]
if sum1 == sum2:
    print("Cross check okay!")
    cross_check = True
else:
    print("Cross check not okay.")

if hor_check and ver_check and cross_check:
    print("This square is magic!")
else:
    print("This square is not magic.")
