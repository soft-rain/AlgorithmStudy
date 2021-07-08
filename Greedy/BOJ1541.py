arr = input().split("-")
plusArr = []
arr2 = []
for i in arr:
    plusArr = i.split("+")
    tot = 0
    for j in plusArr:
        tot += int(j)
    arr2.append(tot)
sum = arr2[0]
for i in range(1, len(arr2)):
    sum -= arr2[i]
print(sum)