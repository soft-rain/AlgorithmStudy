import sys

arr = []
st = list(sys.stdin.readline())
for i in range(len(st)):
    if st[i].isupper():
        if ord(st[i]) + 13 <= 90:
            st[i] = chr(ord(st[i]) + 13)
        else:
            st[i] = chr(ord(st[i]) - 13)

    elif st[i].islower():
        if ord(st[i]) + 13 <= 122:
            st[i] = chr(ord(st[i]) + 13)
        else:
            st[i] = chr(ord(st[i]) - 13)
for i in range(len(st)):
    print(st[i], end="")
