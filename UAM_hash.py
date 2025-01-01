from collections import defaultdict

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

hashmap = defaultdict(set)

for log in logs:
    hashmap[log[0]].add(log[1])
    
ans = [0]*k
val_count = []

for val in hashmap.values():
    val_count.append(len(val))

for i in range(len(val_count)-1):
    ans.insert(i+1, val_count[i])

print(ans)

