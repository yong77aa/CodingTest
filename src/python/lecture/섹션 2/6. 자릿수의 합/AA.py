# import sys
# sys.stdin = open("in2.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

# 각 자리수의 합을 리턴하는 함수
def digit_sum(x):
    str_x = str(x)
    result = 0
    for i in str_x:
        result += int(i)

    return result


result = arr[0]  # 실제 결과값
max_value = digit_sum(arr[0])  # 자리수 최소값
for index, val in enumerate(arr):
    tot = digit_sum(val)
    # print("%d %d" %(val, tot))
    if tot > max_value:
        max_value = tot
        result = val

print(result)