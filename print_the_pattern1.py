rows = int(input("Number of rows: "))
print("\nPattern #1")
for i in range(rows):
    for j in range(i+1):
        print(i+1, end="")
    print()

print("\nPattern #2")
for i in range(rows):
    for j in range(1, i+2):
        print(j, end="")
    print()

print("\nPattern #3")
for i in range(rows):
    for j in range(1, i+2):
        print(2*j-1, end=" ")
    print()

print("\nPattern #4")
for i in range(rows):
    for j in range(1, i+2):
        if j % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
# --------------------------------------

print("\nR e v e r s e: ")
print("\nPattern #1")
for i in range(rows):
    for j in range(rows-i):
        print(rows-i, end="")
    print()

print("\nPattern #2")
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(j+1, end=" ")
    print()

print("\nPattern #3")
for i in range(rows-1, -1, -1):
    for j in range(1, i+2):
        print(2*j-1, end=" ")
    print()

print("\nPattern #4")
for i in range(rows-1, -1, -1):
    for j in range(1, i+2):
        if j % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

