rows = int(input("Number of rows: "))
start = 1
teller = 1

print("Pattern #1:")
for i in range(0, rows):    # number of rows
    for j in range(i + 1):  # number of numbers in each row
        print((start*teller)**2, end=' ')
        teller += 1
    print()

print("\nPattern #2:")
print()
counter = 1
for i in range(1, rows + 1):    # number of rows
    counter += i
    for j in reversed(range(counter-i, counter)):  # number of numbers in each row
        print(j, end=' ')
    print()

print("\nPattern #3:")
alfabet = []
teller = 0
# Make list with all letters:
for i in range(ord('a'), ord('z')+1):
    alfabet.append(chr(i).upper())

for i in range(0, rows+1):  # elke rij een regel
    for j in range(0, teller):
        print(alfabet[0], end="")
        alfabet.append(alfabet.pop(0))
    print()
    teller += 2

print("\nPattern #4:")
print()
for i in range(0, rows):
    print(3*"#"+i*"#")
for i in range(rows, -1, -1):
    print(3*"#"+i*"#")

print("\nPattern #5:")
print()
for i in range(rows, -1, -1):
    print(3*"#"+i*"#")
for i in range(1, rows):
    print(3*"#"+i*"#")

