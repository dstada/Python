'''
Challenge Program to check if a matrix is owl matrix
enter the rows of your matrix in different lines in input
with each element seperated by a comma.
ex : 1,1,1,1 (is a single row of matrix with 1 in each column)

After entering the last row, enter 'e' in new line to stop inputs
Entering 'E' is very important or it will show error

ex: 1,1,1,1
    1,1,1,1
    1,1,1,1
    1,1,1,1
    e
Here we have input an owl matrix of 4x4 with 1 in each element and
e at final line indicates end of taking inputs

i commented on most of the code, so run it have fun and if you like it
consider leaving an upvote, all questions/suggestions welcome, Thank you
'''

def create_matrix(): # takes input of rows from user
    def take_row(row):
        lst = row.split(',')
        return lst
    matrix = []
    while True:
        inp = input("enter single matrix row or 'e' to stop\n")
        if inp == 'e' or inp == 'E' or inp == '':
            break
        else:
            matrix.append(take_row(inp)) #creates matrix from rows
    return  matrix

def check_optimum_len(matrix): # check matrix symmetry
    a = len(matrix)
    if a % 2 != 0: # checks for even number of rows
        return False
    else:
        for _ in matrix:
            if len(_) != a: # checks every row has elements equal to
                return False      # number of rows
        else:
            return  True

def check_owl(matrix):
    i,j,n = 0,0,len(matrix) - 1
    while i < int(len(matrix)/2):
        while j < int(len(matrix)/2): # checks for owl matrix condition
            if (matrix[i][j] == matrix[i][n - j] and
                matrix[i][j] == matrix[n - i][j] and
                matrix[i][j] == matrix[n - i][n - j]):
                    j+=1
            else:
                return False
        i,j = i+1,0  # resetting the counter which iterates over row elements to zero
    return True


if __name__ == "__main__":
    mat = create_matrix()
    print('\n',check_optimum_len(mat) and check_owl(mat))

