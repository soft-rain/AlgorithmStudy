N = list(input())
sum = 0
if "0" in N:
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 3 == 0:
        N.sort()
        N.reverse()
        print("".join(N))
    else:
        print(-1)
else:
    print(-1)