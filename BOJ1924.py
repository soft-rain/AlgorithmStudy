x, y = map(int, input().split())

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
dayCnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
for i in range(0, x - 1):
    day += dayCnt[i]
day = (day + y) % 7
print(week[day])
