# 시뮬레이션 문제
# 하나씩 따라가면서 코드로 구현

n, k = map(int, input().split())  # n: 어항의 수, k: 차이
arr = list(map(int, input().split()))

while True:
    # 최솟값 구해서 하나씩 더하기
    min_temp = min(arr)
    for i in range(arr):
        if min_temp == arr[i]:
            arr[i] += 1

