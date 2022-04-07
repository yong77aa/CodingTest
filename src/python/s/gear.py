import copy


# 톱니바퀴 회전 함수
def rotate(num, direction):
    global gears

    if direction == 1:
        copy_gear = copy.deepcopy(gears[num-1])
        # 시계 방향
        for i, val in enumerate(gears[num-1]):
            if i == len(gears[num-1])-1:
                # 톱니바퀴의 마지막
                gears[num-1][i] = copy_gear[0]  # 마지막 값이 첫번째 값으로 바뀜
            else:
                gears[num-1][i] = copy_gear[i-1]

    else:
        copy_gear = copy.deepcopy(gears[num-1])
        # 반시계 방향
        for i, val in enumerate(gears[num-1]):
            if i == 0:
                # 톱니바퀴의 첫번째
                gears[num-1][i] = copy_gear[len(gears[num-1])-1]  # 첫번째 위치가 마지막으로 감
            elif i != len(gears[num-1])-1:
                gears[num-1][i] = copy_gear[i-1]

# 왼쪽 톱니바퀴 체크
def check_left(start, direction):
    global gears

    if start != 1 or gears[start][6] != gears[start-1][2]:
        rotate(direction, gears[start-2])  # 회전
        check_left(start-1, -direction)

# 오른쪽 톱니바퀴 체크
def check_right(start, direction):
    global gears

    if start != 4 or gears[start][2] != gears[start+1][6]:
        rotate(direction, gears[start])  # 회전
        check_right(start+1, -direction)

# 각 톱니바퀴 점수의 합
def cal_result():
    global gears, result

    for index, val in enumerate(gears):
        print("톱니바퀴 결과 : ", val)
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


gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotate_info = [list(map(int, input().split())) for _ in range(k)]  # 회전시킨 톱니바퀴 번호/ 1: 시계, 2: 반시계
result = 0

for i in rotate_info:
    # 왼쪽 체크
    check_left(i[0], -i[1])
    # 오른쪽 체크
    check_right(i[0], -i[1])
    # 회전
    rotate(i[0], i[1])


# 결과 계산
cal_result()
print("결과: ", result)
