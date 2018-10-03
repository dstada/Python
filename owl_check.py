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
        matrix_array.append(nmbrs2)
        next_line = input("Another line? [j/n]")


def check_matrix():
    pass



if __name__ == "__main__":
    # make matrix with input
    make_matrix()
    # check if matrix is owl
    check_matrix()

