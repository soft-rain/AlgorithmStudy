N, K = map(int, input().split())
coin = []
count = 0
for i in range(N):
    coin.append(int(input()))

coin.sort()
coin.reverse()

for i in range(N):
    if K>=coin[i]:
        count += K // coin[i]
        K %= coin[i]
print(count)