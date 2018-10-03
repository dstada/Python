"""Josephus Problem

N people (numbered 1 to N) are standing in a circle. Person 1 kills Person 2 with a sword and gives it to Person 3. Person 3 kills Person 4 and gives the sword to Person 5. This process is repeated until only one person is alive.

Task:
(Medium) Given the number of people N, write a program to find the number of the person that stays alive at the end.
(Hard) Show each step of the process.
"""

try:
    nbr = int(input("Give number: "))
except:
    print("Number is no integer.")

persons = [i+1 for i in range(nbr)]
print(persons)
while len(persons) > 1:
    print("Person {} shoots person {}. Survivor(s): ".format(persons[0], persons[1]))
    persons.append(persons.pop(0))
    persons.pop(0)
    print(persons)

