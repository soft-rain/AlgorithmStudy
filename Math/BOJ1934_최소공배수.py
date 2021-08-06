import sys

T = int(sys.stdin.readline())

# GCD
def gcd(n, m):

    while m > 0:
        n, m = m, n % m
    return n


# LCM
def lcm(n, m):
    return n * m // gcd(n, m)


for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(lcm(n, m))
