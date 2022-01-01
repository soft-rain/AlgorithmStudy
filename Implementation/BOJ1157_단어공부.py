word = input().lower()
words = list(set(word))
cnt = []
for i in words:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(words[(cnt.index(max(cnt)))].upper())