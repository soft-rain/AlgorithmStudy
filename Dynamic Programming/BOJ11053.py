N = int(input())
A = list((map(int, input().split())))
print(A)
dp = [1] * N
for i in range(N):
    print("i ", i)
    for j in range(i):
        print("j ", j)
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            print("통괴")
            print(dp)
print(max(dp))