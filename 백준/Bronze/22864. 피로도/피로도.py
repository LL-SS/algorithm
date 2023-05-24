a, b, c, m = list(map(int, input().split((' '))))

fatigue = 0
ans = 0

for i in range(24):
    if fatigue + a <= m:
        fatigue += a
        ans += b

    else:
        fatigue -= c

        if fatigue < 0:
            fatigue = 0

print(ans)