import sys
from itertools import combinations

# GCD
def gcd(n, m):

    while m > 0:
        n, m = m, n % m
    return n


n = int(sys.stdin.readline())
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in list(combinations(arr[1:], 2)):
        if i[0] > i[1]:
            ans += gcd(i[0], i[1])
        else:
            ans += gcd(i[1], i[0])
    print(ans)
