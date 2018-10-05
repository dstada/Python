"""String Rotations

Create a function that accepts a string argument and returns an array of strings,
which are shifted versions of the argument string.

Sample Input
"Hello"

Sample Output
["elloH", "lloHe", "loHel", "oHell", "Hello"]

As you can see from the example above, each element shifts the first character of the previous version to the end.
The original string should be included in the output array. The order matters; each element of the output array
should be the shifted version of the previous element.
The output array should have the same length as the input string.
The function should return an empty array when a zero-length String is provided as the argument.
"""


def rotate_word():
    outpt = []  # list of words
    wrd = input("Give a word:")
    arr = []
    # Convert input to list of letters:
    for i in wrd: arr.append(i)
    for q in range(0, len(arr)):
        # Convert list of letters to a string:
        nw_wrd = ""
        for x in arr:
            nw_wrd = nw_wrd + x
        outpt.append(nw_wrd)
        # Rotate the word one position:
        arr.append(arr.pop(0))
    print(outpt)


if __name__ == "__main__":
    rotate_word()
