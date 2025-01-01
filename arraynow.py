A = [2,3,1]
B = [3,1,2]
ans = []
for i in range(len(A)-1):
    count = 0
    if A[i] == B[i]:
        count += 1
    ans[i].append(count)
print(ans)