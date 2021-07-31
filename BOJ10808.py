alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

st = list(input())
<<<<<<< HEAD
=======
print(st)
>>>>>>> 96fab5c376adb98e6a24699144b9b9e7bc57334d

for i in range(26):
    ans = st.count(alphabet[i])
    print(ans, end=" ")