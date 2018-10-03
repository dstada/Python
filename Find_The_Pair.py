nmbr_set = [1, 2, 4, 4]
# total = input("Give number: ")


# for i in range(0,len(nmbr_set)):
#     if nmbr_set[i] + nmbr_set[i+1] == total:
#         print("totaal bereikt")
#     else:
#         if nmbr_set[i] + nmbr_set[i+2] == total:
#             print("totaal bereikt")


import itertools

stuff = [1, 2, 3]
for L in range(2, len(stuff)):
    for subset in itertools.combinations(stuff, L):
        print(subset)
        totaal = (subset[0]+subset[1])
        if totaal == 5:
            print("Match gevonden")

print(itertools.combinations('ABCD', 2))

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

combinations(nmbr_set, 4)