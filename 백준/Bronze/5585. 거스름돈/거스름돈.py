price = int(input())

coin = [500, 100, 50, 10, 5, 1]

change = 1000 - price

answer = 0

for i in coin:
    while change >= i:
        change -= i
        answer += 1

print(answer)