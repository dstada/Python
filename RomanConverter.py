list = ((1000, 'M'), (900, 'CM'), (500, 'D'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

c=input('Enter roman or arabic number: ')
if c.isalpha():     # in ROMEINSE CIJFERS
    c = c.upper()
    res = 0
    # lijst doorlopen met steeds cijfer en romeins teken erbij
    for arabic, roman in list:
        print(arabic, roman)
        while c.startswith(roman):  # als string start met iets uit de lijst:
            c = c[len(roman):]      # c wordt 
            res += arabic
    print('Arabic number:', res)
elif c.isdigit:     # in EEN GETAL
    c = int(c)
    res = ''
    for arabic, roman in list:
        while c > arabic:
            c -= arabic
            res += roman
    print('Roman number:', res)



