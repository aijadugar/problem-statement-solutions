nums = [2,2,2]

ans = []

for num in nums:
    n = str(num)
    r = n[::-1]
    ans.append(int(r))


print(len(set(nums + ans)))