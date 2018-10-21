# input format ax+b=c or c=b+ax
# Examples: -23.5x + 33.7 = 234    456 = -33.3 + 54x
eq = str(input())

a = []
b = []
c = []
plus = []
minus = []
print(eq, '\n')
eq_l = list(range(len(eq)))
print(eq_l)
# delete spaces
for i in eq_l:
    eq_l[i] = eq[i]
count_space = eq_l.count(' ')
for i in range(count_space):
    eq_l.remove(' ')

equal = eq_l.index('=')
to_x = eq_l.index('x')


# # function for find coeffs
# def section(i, list_1, section_l, range_1, range_2):
#     for i in range(range_1, range_2):
#         try:
#             float((list_1[i]))
#         except ValueError:
#             if list_1[i] == '-':
#                 section_l.append(list_1[i])
#             elif list_1[i] == '.':
#                 section_l.append(list_1[i])
#         else:
#             section_l.append(list_1[i])
#
#
# # if ax+b=c
# if equal > to_x:
#     section(i, eq_l, a, 0, to_x)
#     section(i, eq_l, b, to_x, equal)
#     section(i, eq_l, c, equal, len(eq_l))
#
#     A = float(''.join(a))
#     B = float(''.join(b))
#     C = float(''.join(c))
#     print('a=', A, ' b=', B, ' c=', C)
#     print('x=', (C - B) / A)
# # if c=b+ax worked hard on it
# else:
#     section(i, eq_l, c, 0, equal)
#
#     for i in range(equal):
#         eq_l.pop(0)
#
#     for i in range(len(eq_l)):
#         if eq_l[i] == '+':
#             plus.append((eq_l.index('+', i, len(eq_l))))
#         elif eq_l[i] == '-':
#             minus.append((eq_l.index('-', i, len(eq_l))))
#
#     if len(plus) == 1 and len(minus) <= 1:
#         section(i, eq_l, b, 0, eq_l.index('+'))
#         section(i, eq_l, a, eq_l.index('+'), len(eq_l))
#     elif len(minus) == 2:
#         section(i, eq_l, b, 0, minus[1])
#         section(i, eq_l, a, minus[1], len(eq_l))
#     else:
#         section(i, eq_l, b, 0, eq_l.index('-'))
#         section(i, eq_l, a, eq_l.index('-'), len(eq_l))
#     C = float(''.join(c))
#     B = float(''.join(b))
#     A = float(''.join(a))
#     print('a=', A, ' b=', B, ' c=', C)
#     print('x=', (C - B) / A)