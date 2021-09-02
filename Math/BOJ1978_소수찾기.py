import sys

N = int(sys.stdin.readline())

arr = list(map(int, input().split()))
answer = 0
for i in arr:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        answer += 1
print(answer)