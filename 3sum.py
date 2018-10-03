from itertools import combinations

nums = [-1, 0, 1, 2, -1, -4]
result = []

for lst in combinations(nums, 3):
    if sum(lst) == 0:
        result.append(lst)

if len(result) == 0:
    print("No triplets found.")
else:
    for j in range(0,len(result)):
        # print(result[j])
        for k in result[j]:
            print(k, end='')
