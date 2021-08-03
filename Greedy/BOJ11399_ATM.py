N = int(input())
wait = list(map(int, input().split()))
wait.sort()
time = 0
for i in range(N):
    for j in range(i + 1):
        time += wait[i]
print(time)


N = int(input())
wait = list(map(int, input().split()))
wait.sort()
time = 0
for i in range(N):
    time += wait[i] * (N - i)
print(time)
