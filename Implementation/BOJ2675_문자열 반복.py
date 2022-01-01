n = int(input())
for i in range(n):
    R, S = input().split()
    res = ""
    for i in S:
        res += int(R) * i
    print(res)