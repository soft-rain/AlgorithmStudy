i = 1
while True:
    total = 0
    L, P, V = map(int, input().split())
    if [L, P, V] == [0, 0, 0]:
        break
    else:
        total = V // P * L
        if V % P > L:
            total += L
        else:
            total += V % P
    print("Case ", end="")
    print(i, end="")
    i += 1
    print(": ", end="")
    print(total)
