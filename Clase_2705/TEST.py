l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3]

for i in range(len(l1) + 1):
    print(l1[i : len(l2) + i])
