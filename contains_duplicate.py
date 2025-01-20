nums = [1,5,9,1,5,9]
indexDiff = 2
valueDiff = 3

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if (i != j) and (abs(i-j) <= indexDiff) and (abs(nums[i] - nums[j]) <= valueDiff):
            print(True)

print(False)