import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().split()))
arr.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])
