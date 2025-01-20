import math
citations = [3,0,6,1,5]

total = 0
for i in citations:
    total += i

print(math.floor(total / len(citations)))
    
