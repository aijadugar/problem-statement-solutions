from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = []
hashmap = defaultdict(list)

for s in strs:
    sorted_str = tuple(sorted(s))
    hashmap[sorted_str].append(s)

for val in hashmap.values():
    ans.append(val)
    
print(ans)