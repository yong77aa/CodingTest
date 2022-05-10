# 백준알고리즘 https://www.acmicpc.net/problem/1931
# 가장 먼저 끝나는 회의를 먼저 선택

n = int(input())
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort(key=lambda x: (x[1], x[0]))

result = 1
endTime = time[0][1]
for i in range(1, n):
    if time[i][0] >= endTime:
        result += 1
        endTime = time[i][1]

print(result)
