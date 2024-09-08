def wordcheck(s, wordset):
    if len(s)==0:
        return 1
    for i in range(1, len(s) + 1):
        if s[:i] in wordset:
            if wordcheck(s[i:], wordset):
                return 1

    return 0

s=input()
wordset=set(input())
print(wordcheck(s, wordset))
