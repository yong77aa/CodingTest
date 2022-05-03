# 연산자를 끼워넣어서 결과를 도출함
# 첫째 줄에는 수의 개수
# 둘째 줄에는 수열
# 셋째 줄에는 덧셈 뺄셈 곱셈 나눗셈의 개수
# 각 식의 최댓값과 최솟값을 출력함

import sys

def dfs(index, now):
    global n, arr, plus, minus, multiple, divide, max_value, min_value

    if index == n:  # 더 이상 연산할 수가 없는 경우
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    else:
        # 해당 연산자의 개수를 하나 줄이고
        # x의 값을 하나 증가시켜서 다음 숫자를 탐색하게 한 뒤, 연산한 뒤의 값을 넣음
        if plus > 0:
            plus = plus - 1
            dfs(index+1, now + arr[index])
            plus = plus + 1
        if minus > 0:
            minus = minus - 1
            dfs(index+1, now - arr[index])
            minus = minus + 1
        if multiple > 0:
            multiple = multiple - 1
            dfs(index+1, now * arr[index])
            multiple = multiple + 1
        if divide > 0:
            divide = divide - 1
            dfs(index+1, int(now / arr[index]))
            divide = divide + 1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    plus, minus, multiple, divide = map(int, input().split())

    max_value = -1000000001
    min_value = 1000000001

    dfs(1, arr[0])  # 첫번째 인덱스 및 첫번째 수열의 값을 넣어서 재귀 시작
    print(max_value)
    print(min_value)