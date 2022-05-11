# 백준알고리즘 https://www.acmicpc.net/problem/1080

n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    temp = list(map(int, input()))
    a.append(temp)

for i in range(n):
    temp = list(map(int, input()))
    b.append(temp)



print(a)
print(b)