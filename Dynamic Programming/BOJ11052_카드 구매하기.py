N = int(input())
arr = [0]
temp = list(map(int, input().split()))
for i in range(len(temp)):
    arr.append(temp[i])
dp = [0] * (N + 1)
for i in range(N + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], arr[j] + dp[i - j])
print(dp[N])