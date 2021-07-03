N, M = map(int, input().split())
#  N 세로 M 가로
if N == 1 or M == 1:
    print(1)
elif N == 2:
    print(min(4, (M - 1) // 2 + 1))
elif M <= 6:
    print(min(4, M))
else:  ## 세로가 3이상, 가로가 7이상일 때
    print(M - 7 + 5)
