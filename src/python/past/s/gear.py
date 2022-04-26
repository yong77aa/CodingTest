from collections import deque

# 왼쪽 톱니바퀴 체크
def check_left(start, direction):
    if start < 1:
        return

    if gears[start][6] != gears[start-1][2]:
        check_left(start-1, -direction)
        gears[start-1].rotate(-direction)  # 회전

# 오른쪽 톱니바퀴 체크
def check_right(start, direction):
    if start > 2:
        return

    if gears[start][2] != gears[start+1][6]:
        check_right(start+1, -direction)
        gears[start+1].rotate(-direction)  # 회전

# 각 톱니바퀴 점수의 합
def cal_result():
    global gears, result

    for index, val in enumerate(gears):
        # index: 톱니바퀴 번호
        if index == 0:
            if val[0] == 1:
                result += 1
        elif index == 1:
            if val[0] == 1:
                result += 2
        elif index == 2:
            if val[0] == 1:
                result += 4
        else:
            if val[0] == 1:
                result += 8


gears = [deque(map(int, input())) for _ in range(4)]
k = int(input())
rotate_info = [list(map(int, input().split())) for _ in range(k)]  # 회전시킨 톱니바퀴 번호/ 1: 시계, 2: 반시계
result = 0

for i in rotate_info:
    # 왼쪽 체크
    check_left(i[0]-1, i[1])
    # 오른쪽 체크
    check_right(i[0]-1, i[1])
    # 회전
    gears[i[0]-1].rotate(i[1])


# 결과 계산
cal_result()
print(result)
