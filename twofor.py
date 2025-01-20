l = [1, 2, 3, 4]
r = [5, 6, 7, 8]

for i, j in zip(range(len(l)), range(len(r))):
    print(l[i]+r[j])