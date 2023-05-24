inputs = []

for i in range(3):
    inputs.append(list(map(int, input().split(' '))))

n, length, price = inputs[0][0], inputs[1], inputs[2]
i = 0
ans = 0

while i < n - 1:
    to_end = price[i] * sum(length[i:])
    each = 0

    for j in range(i, n - 1):
        each += price[j] * length[j]

    if to_end <= each:
        ans += to_end
        i += n
    else:
        ans += price[i] * length[i]
        i += 1

print(ans)