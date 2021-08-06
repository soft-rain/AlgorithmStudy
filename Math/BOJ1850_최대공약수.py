import sys

# GCD
def gcd(n, m):

    while m > 0:
        n, m = m, n % m
    return n


# LCM
def lcm(n, m):
    return n * m // gcd(n, m)


A, B = map(int, sys.stdin.readline().split())

for i in range(gcd(A, B)):
    print(1, end="")
