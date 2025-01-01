from collections import defaultdict

s = "leetcode"
t = "practice"

ans = 0

hashmap = defaultdict(list)

for c in s:
    if c in hashmap:
        hashmap[c] += 1
    else:
        hashmap[c] = 1
    
for i in t:
    if i not in hashmap:
        ans += 1
    else:
        hashmap[i] -= 1

    if hashmap[i] == 0:
        del hashmap[i]
        
print(hashmap)
print(ans)
    