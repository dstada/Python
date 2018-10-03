"""[ Challenge] Morse Code Converter

User's input can be letters or morse code.
First character of the input says whether it is morse code or text.
Unknown characters are translated to a question mark.

Jun 5th, 2018
By Dick Stada, NL
"""


codes = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '0': '-----'}

text = input('Give some text or morse code: ')
text = text.strip()         # strip whitespace
text = text.lower()         # no capitals

if text[0] in codes:    # Checks if first character is letter or code
    # It's text
    for letter in text.lower():
        if letter not in codes:
            if letter == " ":       # space will be space
                print(" ", end="")
            else:                   # unknown character
                print("? ", end="")
        else:
            print(codes[letter] + " ", end="")
else:   # It is morse code
    # Split the morse code characters
    morse_code = text.split()
    for q in morse_code:
        print(list(codes.keys())[list(codes.values()).index(q)] + " ", end="")
