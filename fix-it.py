'''[Assignment] Let Fix This

You have given an input string s and an array a contain number of strings. Create an program that return all the string that has s as prefix and suffix.

Input :: s = he ,a = [heat,heal,hair,the]
Outputs :: Prefix : heat, heal
         Suffix : the

Presumption: s is shorter than the elements of a

'''

s = "he"
a = ["heat", "heal", "hair", "the"]

print("Prefix: ", end="")       # end for printing on the same line
for i in range(0, len(a)):      # for every element in a:
    for x in range(0, len(s)):  # for every character in s:
        if s[x] == a[i][x]:     # characters are the same
            if x + 1 == len(s):
                print(a[i]+" ", end="")
        else:
            break

print("\nSuffix: ", end="")
for i in a:                     # for every word in a:
    counter = 1
    for j in reversed(s):       # for every character in a:
        if j == i[len(i) - counter]:    # when all chars of a have been checked
            if counter == len(j):
                print(i, end="")
            counter += 1

