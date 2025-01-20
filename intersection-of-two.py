nums1 = [1,2,2,1]
nums2 = [2,2]

ans = set()

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            ans.add(nums1[i])

print(list(ans))