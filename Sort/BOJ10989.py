import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] = arr[num] + 1
print(arr)
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)