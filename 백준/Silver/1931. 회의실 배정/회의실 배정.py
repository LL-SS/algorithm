n = int(input())
meetings = []
ans = []

for i in range(n):
    time = input().split(' ')
    meetings.append((int(time[0]), int(time[1])))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

ans.append(meetings[0])

for i in range(1, n):
    if ans[-1][1] <= meetings[i][0]:
        ans.append(meetings[i])

print(len(ans))