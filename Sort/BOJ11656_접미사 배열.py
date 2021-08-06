import sys

arr = []
S = str(sys.stdin.readline().strip())
for i in S:
    arr.append(S)
    S = S[1:]
arr.sort()
for i in arr:
    print(i)