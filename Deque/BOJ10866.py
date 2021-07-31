import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()


for i in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == "push_back":
        d.append(a[1])
    elif a[0] == "push_front":
        d.appendleft(a[1])
    elif a[0] == "pop_front":
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    elif a[0] == "pop_back":
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(d))
    elif a[0] == "empty":
        if len(d) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    elif a[0] == "back":
        if len(d) != 0:
            print(d[len(d) - 1])
        else:
            print(-1)
