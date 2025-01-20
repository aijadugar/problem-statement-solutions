# Input
words = ["a", "aba", "ababa", "aa"]

for i in range(len(words)):
    for j in range(len(words)):
        if words[j].startswith(words[i]) and words[i].endswith(words[i]):
            print(words[i])