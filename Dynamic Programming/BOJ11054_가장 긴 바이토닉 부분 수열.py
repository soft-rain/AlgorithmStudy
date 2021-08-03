N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
dpp = [1] * N
res = [0] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[i] > arr[j]:
            dpp[i] = max(dpp[i], dpp[j] + 1)

for i in range(N):
    res[i] = dp[i] + dpp[i] - 1
print(max(res))
