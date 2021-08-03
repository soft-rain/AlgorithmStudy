import sys

N = int(sys.stdin.readline())

for i in range(N):
    cnt = 0
    stack = []
    ps = list(sys.stdin.readline())
    for j in range(len(ps)):
        if ps[j] == "(":
            stack.append(ps[j])
        elif ps[j] == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                cnt = 1
                break
    if len(stack) == 0 and cnt == 0:
        print("YES")
    elif len(stack) != 0 and cnt == 0:
        print("NO")
