import sys
sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())

temp_sum = [0] * (n+m+1)
max = -2147000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        temp_sum[i+j] += 1

for i in range(n+m+1):
    if temp_sum[i] > max:
        max = temp_sum[i]

for i in range(n+m+1):
    if temp_sum[i] == max:
        print(i, end=' ')
