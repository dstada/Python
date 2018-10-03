'''Write a program to remove all the special characters from a given string and print the result.
Some examples of special characters: "@#₹_ƒ&-+`()/*{}€¥$¢~"

For example:
Input:
1. "H@e#&l+l/*o"
2. "$¥W¢πO}R|%L&@D"

Output:
1. Hello
2. WORLD


By Dick Stada, the Netherlands
'''

import re
test_strings = ("H@e#&l+l/*o", "$¥W¢πO}R|%L&@D")
for strng in test_strings:
    print(re.sub('[^A-Za-z0-9]+', '', strng))

