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
    # for x in (0, 5):
        print(x)


if __name__ == "__main__":
    check_matrix(make_matrix())  # First make the matrix, then check if it is an owl.



