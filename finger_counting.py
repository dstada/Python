"""[M💙 Challenge] Finger Counting

Monday Blue 💙 Challenge Series #13

Let's do some counting this week! This time we will need to determine which finger was last counted using Sololand's arithmetic. Assume that we will use both our hands with 5 fingers, here's how we do the counting start with the left-hand:-

Left Hand       Right Hand
Thumb: 1        Thumb: 6
Index: 2        Index: 7
Middle: 3       Middle: 8
Ring: 4         Ring: 9
Baby: 5         Baby: 10

Once we reached to the end, we will continue the count backwards and here's the label for each of the fingers count up to 31:-

Left Hand
Thumb: 1, 19
Index: 2, 18, 20
Middle: 3, 17, 21
Ring: 4, 16, 22
Baby: 5, 15, 23

Right Hand
Thumb: 6, 14, 24
Index: 7, 13, 25, 31
Middle: 8, 12, 26, 30
Ring: 9, 11, 27, 29
Baby: 10, 28

TASK
Write a program to accept an integer and determine which finger was last counted with the given number.

TEST CASE
10 ➡ "Baby Finger (Right)"
22 ➡ "Ring Finger (Left)"
25 ➡ "Index Finger (Right)"
42 ➡ "Thumb (Right)"
101 ➡ "Ring Finger (Right)"
1001  ➡ "Ring Finger (Right)"
25122017  ➡ "Ring Finger (Right)"
31122017  ➡ "Middle Finger (Left)"

BONUS
Clear-cut and optimized approach is encouraged.

Happy Coding!!!
--------------------------------------
By: Dick STADA, NL
October 2018

This was helpful:

    1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30
    d	w	m	r	p	dr	wr	mr	rr	pr
                                       pr	rr	mr	wr	dr	p	r	m	w	d
                                                                          d	w	m	r	p	dr	wr	mr	rr	pr
                                                                                                             pr	rr	mr
"""


def take_finger(nmbr):
    hand = ["Thumb (Left)", "Index Finger (Left)", "Middle Finger (Left)", "Ring Finger (Left)", "Baby Finger (Left)",
            "Thumb (Right)", "Index Finger (Right)", "Middel Finger (Right)", "Ring Finger (Right)",
            "Baby Finger (Right)"]
    time_nine = nmbr // 9       # How many times fits 9 in number
    rest = nmbr % 9             # What's the rest after dividing by 9
    if time_nine % 2 == 0:      # Even
        print("Finger: {}".format(hand[rest - 1]))
    else:                       # Odd
        print("Finger: {}".format((list(reversed(hand)))[rest - 1]))


if __name__ == "__main__":
    take_finger(int(input("Give number: ")))
