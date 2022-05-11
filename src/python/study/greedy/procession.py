# 백준알고리즘 https://www.acmicpc.net/problem/1080
# 가장 첫번째 값부터 비교해나감

n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    temp = list(map(int, input()))
    a.append(temp)

for i in range(n):
    temp = list(map(int, input()))
    b.append(temp)


def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if a[x][y] == 0:
                a[x][y] = 1
            else:
                a[x][y] = 0


result = 0
if (n < 3 or m < 3) and a != b:
    result = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                result += 1
                change(i, j)

if result != -1:
    if a != b:
        result = -1

print(result)