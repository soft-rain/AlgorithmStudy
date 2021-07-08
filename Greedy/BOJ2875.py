# 여학생 N, 남학생 M, 참여해야하는 인원 K
# 2명의 여학생, 1명의 남학생 무조건 참여해야 함

N, M, K = map(int, input().split())
t = 0 # 팀 개수
while N>=2 and M>=1 and N+M>=K+3:
    t += 1
    N -= 2
    M -= 1
print(t)

