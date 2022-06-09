# import sys
# sys.stdin = open("in1.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(arr[i] + arr[j] + arr[m])

result = list(result)
result.sort(reverse=True)

print(result[k-1])