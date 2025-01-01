nums = [1,3,4,1,2,3,1]

hashmap = {}

for ele in nums:
    if ele in hashmap:
        hashmap[ele] += 1
    else:
        hashmap[ele] = 1
        
ans = []

while hashmap:
    for key in list(hashmap.keys()):
        ans.append(hashmap[key])
        if hashmap[key] > 0:
            hashmap[key] -= 1
            if hashmap[key] == 0:
                del hashmap[key]

    print(ans)
        
    
        


