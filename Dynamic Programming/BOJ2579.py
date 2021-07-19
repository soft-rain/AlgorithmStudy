n = int(input())
<<<<<<< HEAD
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
=======
arr = []
for i in range(n):
    arr.append(int(input()))
>>>>>>> 7c096f77037dae0fa5face960f8a20e8aa736504
dp = [0] * n
dp[0] = arr[0]
dp[1] = max(dp[0], arr[0] + arr[1])
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
for i in range(3, n):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])
<<<<<<< HEAD
    print(dp)
print(dp[n - 1])
=======

print((dp[n]))
>>>>>>> 7c096f77037dae0fa5face960f8a20e8aa736504
