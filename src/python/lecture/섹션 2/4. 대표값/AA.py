# import sys
# sys.stdin = open("in4.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
avg = int(sum(arr) / len(arr) + 0.5)

diff_arr = []
for i in arr:
    diff_arr.append(i - avg)

result = 0
min_temp = 2147000000
for index, i in enumerate(diff_arr):
    if abs(i) < min_temp:
        # 절대값이 최소값인 경우 결과 갱신
        min_temp = abs(i)
        result = index+1
    elif abs(i) == min_temp:
        # 절대값이 같은 경우
        if not(min_temp > 0 and i > 0) and i > 0:
            # 둘 다 0보다 큰 경우를 제외하고 새로운 값이 0보다 크면 더 큰 값이니까 결과 갱신
            result = index+1

print("%d %d" %(avg, result))
