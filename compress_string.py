test = "abdddeefghhhijkkk"
compr = test[0]
teller = 1
for i in range(1, len(test)):
    if test[i] == test[i-1]:
        teller += 1
    else:
        if teller > 1:
            compr = compr + str(teller) + test[i]
        else:
            compr = compr + test[i]
        teller = 1

print(compr)


