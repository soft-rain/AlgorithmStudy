import sys

n, m = map(int, sys.stdin.readline().split())
# GCD
def gcd(n, m):

    while m > 0:
        n, m = m, n % m
    return n


# LCM
def lcm(n, m):
    return n * m // gcd(n, m)


print(gcd(n, m), lcm(n, m), sep="\n")
