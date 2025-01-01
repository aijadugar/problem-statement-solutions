from collections import defaultdict

A = [2,3,1]
B = [3,1,2]

hashA = defaultdict(int)
hashB = defaultdict(int)

ans = [0]

for i in range(len(A)):
    hashA[A[i]] += 1
    hashB[B[i]] += 1

    count = 0
    for key in hashA:
        if key in hashB:
            count += 1
    
    if i>=1:
        ans.append(count)
            
print(ans)