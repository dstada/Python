# aantal = int(input("Hoeveel bij hoeveel?"))

rij0 = [1, 0, 0, 0]
print(rij0)
rij1 = []
rij2 = []
rij3 = []

# rij1.append(1)
# print(rij1)
# rij0[0] = 0
# print(rij0)

# berekenen tweede rij (rij1):
for i in range(0, 4):   # voor elk van de vier plekken in de rij:
    print("we gaan nu positie {} doen".format(i))
    if i-1 >= 0 and rij0[i-1] == 1:
        rij1.append(0)
    elif rij0[i] == 1:
        rij1.append(0)
    else:
        rij1.append(1)
        


    # if rij0[i] == 1 or rij0[]:
    #     rij1.append(0)
    #     print("aanvullen lijst1")
    # if i < (len(rij1)-1):
    #     print("i kleiner dan lengte van de list")
    #     if rij0[i+1] == 1:
    #         rij1.append(0)
    # else:
    #     rij1.append(1)

print(rij1)




