"""
RGB to HEX Converter

RGB colors are represented as triplets of numbers in the range of 0-255, representing the red, green and blue components
 of the resulting color.
Each RGB color has a corresponding hexadecimal value, which is expressed as a six-digit combination of numbers
and letters and starts with the # sign.
The numbers and letters in a hex value can be in the range [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F].
The hexadecimal is basically a base 16 representation of the RGB value, which is a base 10 value.
Write a program that takes an RGB color value as input and converts it to its Hexadecimal equivalent.

For Example:
Input: (66, 134, 244)
Hex equivalent: #4286f4

Input: (119, 119, 119)
Hex equivalent: #777777 or #777

By: Dick Stada, NL
November 2018
See: https://www.w3schools.com/colors/colors_picker.asp
and see: https://pypi.org/project/colour/
"""
import colour as colour

color = [256, 256, 256]
while color[0] > 255 or color[1] > 255 or color[2] > 255:
    color = list((map(int, input("Give rgb by three numbers 0-255, separated by a space:").split())))

print(color)


def rgb_to_hex(rgb):
    hexa = ""
    for i in rgb:
        if len(str(hex(i))) < 4:
            hexa = hexa + "0" + str(hex(i))[2]
        else:
            hexa = hexa + str(hex(i))[2:4]
    hexa = "#" + hexa
    return hexa


hx = rgb_to_hex(color)
print(hx)
print(colour.Color(hx))     # prints name of the colour if it exists
