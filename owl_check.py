def make_matrix():
    print("Give a rule of numbers, separated by a comma")
    # Voeg input toe aan array
    # Vraag of er nog een regel bij moet
    # Ontvang de extra input
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
    print(mat_arr)
    # Tel aantal regels
    print("Aantal cijfers horizontaal: {}".format(len(mat_arr[0])))
    # Eerst checken of elke regel symmetrisch is
    hor_flag = True
    for i in mat_arr:   # voor elke regel:
        if i != i[::-1]:
            hor_flag = False
    print(hor_flag)
    # Nu checken of het verticaal symetrisch is
    print("Aantal regels (verticaal): {}".format(len(mat_arr)))
    nbr_rules = len(mat_arr)
    # Vergelijk eerste en laatste regel:
    print("Laatste regel: {}".format(mat_arr[nbr_rules - 1]))
    print("Eerste regel: {}".format(mat_arr[nbr_rules - nbr_rules]))
    # aantal keer dat er regels moeten worden vergeleken:
    # Aantal regels / 2 (bij oneven hoeft tussenregel niet te worden gecheckt)
    checks = nbr_rules // 2
    print(checks)
    ver_flag = True
    for y in range(0, checks):
        print("Check")
        # Compare the two rules:
        print("Nu kijken naar regel {} en {}.".format(y, nbr_rules - y - 1))
        if mat_arr[y] != mat_arr[nbr_rules - y - 1]:
            print("Vert.check not okay!")
            ver_flag = False
    print(ver_flag)


if __name__ == "__main__":
    check_matrix(make_matrix())  # First make the matrix, then check if it is an owl.



