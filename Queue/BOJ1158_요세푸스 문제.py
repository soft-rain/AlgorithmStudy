import sys

N, K = map(int, sys.stdin.readline().split())
queue = []
answer = []
for i in range(1, N + 1):
    queue.append(i)
num = K - 1
for i in range(N):
    if len(queue) > num:
        answer.append(queue.pop(num))
        num += K - 1
    elif len(queue) <= num:
        num = num % len(queue)
        answer.append(queue.pop(num))
        num += K - 1
print("<", end="")
for i in range(len(answer) - 1):
    print(answer[i], end=", ")
print(f"{answer[len(answer)-1]}>")