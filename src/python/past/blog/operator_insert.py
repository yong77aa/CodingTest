# 연산자를 끼워넣어서 결과를 도출함
# 첫째 줄에는 수의 개수
# 둘째 줄에는 수열
# 셋째 줄에는 덧셈 뺄셈 곱셈 나눗셈의 개수
# 각 식의 최댓값과 최솟값을 출력함

import sys

def dfs(x, now):
    global a, b, c, d, max_value, min_value

    if x == num:  # 더 이상 연산할 수가 없는 경우
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    else:
        # 해당 연산자의 개수를 하나 줄이고
        # x의 값을 하나 증가시켜서 다음 숫자를 탐색하게 한 뒤, 연산한 뒤의 값을 넣음
        if a > 0:
            a = a - 1
            dfs(x+1, now + arr[x])
            a = a + 1
        if b > 0:
            b = b - 1
            dfs(x+1, now - arr[x])
            b = b + 1
        if c > 0:
            c = c - 1
            dfs(x+1, now * arr[x])
            c = c + 1
        if d > 0:
            d = d - 1
            dfs(x+1, int(now / arr[x]))
            d = d + 1


if __name__ == "__main__":
    num = int(sys.stdin.readline())  # 숫자의 개수
    arr = list(map(int, sys.stdin.readline().split()))  # 수열
    a, b, c, d = map(int, sys.stdin.readline().split())  # 덧셈, 뺄셈, 곱하기, 나누기

    # 최대, 최소값
    max_value = -1000000001
    min_value = 1000000001

    dfs(1, arr[0])  # 첫번째 인덱스 및 첫번째 수열의 값을 넣어서 재귀 시작
    print(max_value)
    print(min_value)