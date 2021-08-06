import sys

A, B, C = map(int, sys.stdin.readline().split())
# 1
sum1 = A + B
print(sum1 % C)
# 2
op1 = A % C
op2 = B % C
sum2 = op1 + op2
print(sum2 % C)
# 3
op3 = A * B
print(op3 % C)
# 4
op4 = op1 * op2
print(op4 % C)

# 다른 방법
print(
    (A + B) % C,
    (((A % C) + (B % C)) % C),
    ((A * B) % C),
    ((A % C) * (B % C)) % C,
    sep="\n",
)
