n = int(input())
change = []
ans = []

for i in range(n):
    change.append(int(input()))

for c in change:
    coins = []

    if c >= 25:
        coins.append(str(c // 25))
        c %= 25
    else:
        coins.append('0')

    if c >= 10:
        coins.append(str(c // 10))
        c %= 10
    else:
        coins.append('0')

    if c >= 5:
        coins.append(str(c // 5))
        c %= 5
    else:
        coins.append('0')

    coins.append(str(c))
    ans.append(coins)

for a in ans:
    print(' '.join(a))
