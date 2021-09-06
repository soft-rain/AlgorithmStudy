L, P = map(int, input().split())
tot = L * P
arr = list(map(int, input().split()))
for i in arr:
    i = i - tot
    print(i, end=" ")
