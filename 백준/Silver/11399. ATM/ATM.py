n = int(input())
times = list(map(int, input().split(' ')))
times.sort()
ans = 0

for i in range(n):
    ans += sum(times[:i + 1])

print(ans)