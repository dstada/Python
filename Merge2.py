l1 = [1, 4, 6, 17, 23, 28]
l2 = [2, 7, 20]

merged = []

try:
    while True:
        merged.append((min(l1, l2).pop(0)))
        print(merged, l1, l2, sep=" ")
except:
    pass
finally:
    merged.extend(l1)
    merged.extend(l2)
    print(merged)
