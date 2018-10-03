"""Give a variable number of words, create a program to output the word with the maximum score, based on the following scoring system:
The score of a word is calculated based on its character values, according to this table:
e, a, i, o, n, r, t, l, s, u are equal 1 point
d, g	2 points
b, c, m, p	3 points
f, h, v, w, y 4 points
k 5 points
j, x 8 points
q, z 10 points

The max length of a word is 10 letters.

For example:
input { "This",  "is", "a", "cool" , "Challenge" }
output : Challenge
"""
points = {"e": 1, "a": 1, "i": 1, "o": 1, "n": 1, "r": 1, "t": 1, "l": 1, "s": 1, "u": 1, "d": 2, "g": 2, "b": 3,
          "c": 3, "m": 3, "p": 3, "f": 4, "h": 4, "v": 4, "w": 4, "y": 4, "k": 5, "j": 8, "x": 8, "q": 10, "z": 10 }
# inpt = ["This",  "is", "a", "cool", "Challenge"]
inpt = input("Give some words, separated by space: ")
inpt = inpt.split()
most = 0
for i in inpt:          # For each word:
    tot = 0
    for j in i:         # For each character in word:
        if j.isalpha(): # Only alphanumeric character:
            tot = tot + points[j.lower()]
    if tot > most:
        most = tot
        word_most = i
print("word_most: {}".format(word_most))

