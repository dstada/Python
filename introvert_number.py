'''[ASSIGNMENT] Introvert Numbers
Imagine that all single digit numbers do not like each other and thus one number can not stand together with the other one in one string closer than its own value. Zero is the only friendly number, which can be in contact with others.

TASK:
For given string check if all numbers feel them well (stand far enough from its neighbors).

EXAMPLES:
1. "4000005" -> True
2. "11" -> False

DUS: links en rechts mogen niet dezelfde cijfers staan binnen het aantal posities dat het cijfer is.

EXTRA TASK:
If input string is wrong, print out the shortest corrected string:
1. "10200002" -> "100200002"
2. "110" -> "1010"
'''

inpt = input("Give number: ")
trick = []
for i in range(len(inpt)-1):
    if str(inpt[i]) != "0":
        if inpt[i] == inpt[i+1]:
            trick.append("GG")
if len(trick) == 0:
    print(inpt, "is not an introvert number")
else:
    print(inpt, "is an introvert number")


'''    
def secure(num):
    ori=num
    # ori for original number. Ori will be kept unaltered in order to compare it to the processed numbered when printing.
    # If ori==num then, it means nothing had to be changed and the num was OK.
    mem, i, gap = 0, 0, 0
    # mem is keeping memory of the previous encountered non-zero digit while parsing the string
    # gap is the size of the '0' gap between other digits : '3002' has a gap of 2
    while i < len(num):
        if num[i] == '0':
            gap += 1
        else:
            if (gap < mem or gap < int(num[i])) and mem != 0:
                num = num[:i] + '0' + num[i:]
                gap += 1
            else:
                mem = int(num[i])
                gap = 0
        i += 1
    return num, ori

testset = ('4000005','400302','11','110','0001240022000')

for test in testset:
    num, ori = secure(test)
    print('{} {}{} {}'.format(ori,'xenophobik security was OK'*(ori==num),'had to be secured to'*(ori!=num),num*(ori!=num)))
'''