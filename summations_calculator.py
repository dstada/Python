frm = input("From: ")
to = input("To: ")
exp = input("Choose expression: (+  -  *  /  %  **  // ")
nmbr = input("Type a number: ")

for i in range(int(frm), int(to)):
    print(eval(str(i) + exp + nmbr))

# a = int(input("Enter a number:"))
# b = int(input("Enter another number:"))
# c = input("Enter an operation:")
# sum = 0
# for i in range(a, b + 1):
#     sum += eval(str(i) + str(c))
#
# print(sum)