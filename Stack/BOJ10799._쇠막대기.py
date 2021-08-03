ps = list(input())
count = 0
stack = []

for i in range(len(ps)):
    if ps[i] == "(":
        stack.append("(")

    else:
        if ps[i - 1] == "(":
            stack.pop()
            count += len(stack)

        else:
            stack.pop()
            count += 1

print(count)