이화자판기 = "음료 a = 500 \n음료 b = 800 \n음료 c = 1000 \n"
print("<이화 자판기>")
print(이화자판기)


asum = 0
bsum = 0
csum = 0

for i in range(3):
    drink = str(input("음료의 종류를 입력하세요 : "))
    count = int(input("해당 음료의 수를 입력하세요 : "))
    if drink == "a":
        asum = asum + count
    elif drink == "b":
        bsum = bsum + count
    elif drink == "c":
        csum = csum + count

sum = asum * 500 + bsum * 800 + csum * 1000

print(asum, end=" ")
print(bsum, end=" ")
print(csum, end=" ")
print(sum)
