n, money = list(map(lambda x: int(x), input().split(' ')))

answer = 0
coins = []

for i in range(n):
    coins.insert(0, int(input()))

for coin in coins:
    if money >= coin:
        answer += money // coin
        money = money % coin

print(answer)