# ["as","hero"]

words = ["mass","as","hero","superhero"]

ls = 0
ms = 0
ans = []

for i in range(len(words)):
    for j in range(len(words)):
        if (i != j) and (words[i] in words[j]):
            ans.append(words[i])

print(ans)
            