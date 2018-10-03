n = 3

a = [[chr(i+j) for i in range(n)]for j in range(65,65+n*n,n)]

print(a)
t01 = '90 deg counterclockwise'
rccw90 = lambda x:[[i[-j-1] for i in x]for j in range(n)]
print(rccw90(a))


# List maken van 3 x 3
# n = 3
# a = [[(i+j) for i in range(n)]for j in range(1, 9, 3)]


# named function
# def polynomial(x):
#     return x**2 + 5*x + 4
#
#
# print(polynomial(-4))
#
#
# # lambda
# print((lambda x: x**2 + 5*x + 4)(-4))

