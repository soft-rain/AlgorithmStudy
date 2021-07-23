import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr.append([b, a])
arr.sort()

for i in range(N):
    print(arr[i][1], arr[i][0])