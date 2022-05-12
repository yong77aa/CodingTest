# 백준알고리즘 https://www.acmicpc.net/problem/2138
import copy

# 전구 상태 변경
def state_change(num):
    if num == 0:
        num = 1
    elif num == 1:
        num = 0

    return num


# 계산
def solution(bulb, count):
    if count == 1:
        # 첫번째 전구 스위치를 누름
        bulb[0] = state_change(bulb[0])
        bulb[1] = state_change(bulb[1])

    for i in range(1, n):
        if bulb[i-1] != target[i-1]:
            print("_____ i: " + str(i))
            # 이전 값이 다름
            count += 1
            bulb[i-1] = state_change(bulb[i-1])
            bulb[i] = state_change(bulb[i])
            if not i >= n-1:
                # 마지막 인덱스가 아님
                bulb[i+1] = state_change((bulb[i+1]))

    if bulb == target:
        return count
    else:
        return -1


n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

bulb_1 = copy.deepcopy(bulb)
bulb_2 = copy.deepcopy(bulb)

result_1 = solution(bulb_1, 0)
result_2 = solution(bulb_2, 1)

if result_1 >= 0 and result_2 >= 0:
    # 둘 다 계산 가능
    print(min(result_1, result_2))
elif result_1 >= 0 and result_2 < 0:
    # 첫번째 경우만 성공
    print(result_1)
elif result_1 < 0 and result_2 >= 0:
    # 두번째 경우만 성공
    print(result_2)
else:
    # 둘 다 실패
    print(-1)

