def make_matrix():
    print("Give a rule of numbers, separated by a comma")
    # Voeg input toe aan array
    # Vraag of er nog een regel bij moet
    # Ontvang de extra input
    matrix_array = []
    next_line = "j"
    while next_line == "j" or next_line == "J":
        nmbrs = input("Give line of numbers:")
        print(nmbrs)
        # Split and put in array:
        nmbrs2 = nmbrs.replace(",", " ").split()
        for i in nmbrs2:
            print(i)
        matrix_array.append(nmbrs2)
        next_line = input("Another line? [j/n]")
    return matrix_array


def check_matrix(mat_arr):
    print(mat_arr)
    # Tel aantal regels
    print("Aantal regels (verticaal): {}".format(len(mat_arr)))
    print("Aantal cijfers horizontaal".format(len(mat_arr[0])))


if __name__ == "__main__":
    check_matrix(make_matrix())  # First make the matrix, then check if it is an owl.



