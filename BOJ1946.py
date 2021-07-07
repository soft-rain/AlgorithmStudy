import sys

T = int(sys.stdin.readline())
for i in range(T):

    N = int(sys.stdin.readline())
    arr = []
    for j in range(N):
        score, rank = map(int, sys.stdin.readline().split())
        arr.append([score, rank])
    arr.sort()
    count = 1

    max = arr[0][1]
    for j in range(1, N):
        if max > arr[j][1]:
            count += 1
            max = arr[j][1]
    print(count)
