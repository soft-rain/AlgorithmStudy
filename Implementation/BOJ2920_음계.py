words = list(map(int, input().split()))
if words == sorted(words):
    print("ascending")
elif words == sorted(words, reverse=True):
    print("descending")
else:
    print("mixed")