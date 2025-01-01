from itertools import product
digits = "23"

map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

ans = []

# if digits == '':
#     return []

# if len(digits) == 1:
#     return map[digits[1]]

for key, val in map.items():
    for dig in digits:
        if dig == key:
            ans.append(val)
    
res = [''.join(comb) for comb in product(*ans)]

print(res)

    
