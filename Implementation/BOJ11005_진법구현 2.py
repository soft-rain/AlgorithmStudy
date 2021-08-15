import sys

N, B = map(int, sys.stdin.readline().split())
change = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
while N != 0:
    ans += str(change[N % B])
    N = N // B
print(ans[::-1])
