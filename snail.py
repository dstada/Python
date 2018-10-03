"""A Snail's Journey

Each day the snail climbs up A meters on a tree with H meters in height.
At night it goes down B meters.
Write a program which takes 3 inputs: H, A, B, and calculates how many days it will take for the snail to get to the top of the tree.
Assume H > A > B

For Example:
Input: 15, 1, 0.5
Output: 29 days
"""


height = float(input("Tree height: "))
up = float(input("Distance up: "))
down = float(input("Distance down: "))

days = (height-down)/(up-down)
print("{} days".format(int(days)))