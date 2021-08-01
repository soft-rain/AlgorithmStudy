import sys

while True:

    st = sys.stdin.readline().rstrip("\n")
    lower = upper = num = space = 0
    if not st:
        break
    for i in range(len(st)):
        if st[i].islower():
            lower += 1
        elif st[i].isupper():
            upper += 1
        elif st[i].isdigit():
            num += 1
        elif st[i].isspace():
            space += 1
    print(lower, upper, num, space)
