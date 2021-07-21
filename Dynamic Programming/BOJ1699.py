N = int(input())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = i
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
            ## min함수 쓰면 시간초과 뜸
print(dp[N])
