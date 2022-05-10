# 백준알고리즘 https://www.acmicpc.net/problem/11399
# 당장 소요시간이 적은 사람부터 선택

n = int(input())
times = list(map(int, input().split()))
times.sort()
result = 0

for i in range(len(times)):
    if i == 0:
        result += times[i]
    else:
        for j in range(0, i+1):
            result += times[j]

print(result)