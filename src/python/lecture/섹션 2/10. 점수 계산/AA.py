import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
result = 0

score = 0
for index, val in enumerate(arr):
    if val == 0:
        # 틀림
        continue
    else:
        # 맞음
        if index != 0 and arr[index-1] == 1:
            # 이전에 맞춘 경우 가산점
            score += 1
            result += score
        else:
            # 처음 맞춘 경우
            score = 1
            result += score

print(result)