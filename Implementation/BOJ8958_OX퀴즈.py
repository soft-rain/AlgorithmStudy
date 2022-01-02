n = int(input())
for i in range(n):
    str = input()
    s = list(str)
    sum = 0
    count = 1
    for i in s:
        if i == "O":
            sum += count
            count += 1
        else:
            count = 1
    print(sum)