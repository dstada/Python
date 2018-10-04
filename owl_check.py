'''Owl challenge Sololearn.com
   Asks a matrix of numbers
   and checks if the matrix can be folded
   horizontally and vertically.
   Input must be rules of numbers, separated by commas.

    By: Dick Stada, NL
    October 2018
    TODO: input control
'''


def make_matrix():
    print("Give a rule of numbers, separated by a comma")
    matrix_array = []
    next_line = "j"
    while next_line == "j" or next_line == "J":
        nmbrs = input("Give line of numbers:")
        # Split and put in array:
        nmbrs2 = nmbrs.replace(",", " ").split()
        matrix_array.append(nmbrs2)
        next_line = input("Another line? [j/n]")
    return matrix_array


def check_matrix(mat_arr):
    # Check each rule on symmetricity
    hor_flag = True
    for i in mat_arr:   # for each rule:
        if i != i[::-1]:  # rule and reversed rule must be identical
            hor_flag = False
    # Check vertical symmetry
    nbr_rules: int = len(mat_arr)
    checks = nbr_rules // 2     # with odd number of rules, central rule not checked
    ver_flag = True
    for y in range(0, checks):
        # Compare the two rules:
        if mat_arr[y] != mat_arr[nbr_rules - y - 1]:
            ver_flag = False
    if hor_flag is True and ver_flag is True:
        print("This matrix is owl!")
    else:
        print("This matrix is unfortunately no owl...")


if __name__ == "__main__":
    check_matrix(make_matrix())  # First make the matrix, then check if it is an owl.



