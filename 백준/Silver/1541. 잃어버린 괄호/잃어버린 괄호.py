nums = input().split('-')
ans = 0

for i in range(len(nums)):
    nums[i] = list(map(int, nums[i].split('+')))

ans += sum(nums[0])

for i in range(1, len(nums)):
    ans -= sum(nums[i])

print(ans)