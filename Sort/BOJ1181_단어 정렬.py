n = int(input())
wordlist = []
for i in range(n):
    wordlist.append(input())

wordlist = list(set(wordlist))
wordlist.sort(key=lambda x: (len(x), x))
for i in wordlist:
    print(i)