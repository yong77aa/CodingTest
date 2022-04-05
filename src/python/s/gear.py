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
def check_left(num, direction):
    global gears

    if num != 1:
        # 맨 왼쪽 톱니바퀴는 왼쪽을 체크하지 않음
        if gears[num-1][6] != gears[num-2][3]:
            # 다른 극인 경우
            if direction == 1:
                # 원래 톱니바퀴가 시계 방향으로 회전
                rotate(-1, gears[num-2])  # 반시계 방향으로 회전
            else:
                # 반시계
                rotate(1, gears[num-2])

# 오른쪽 톱니바퀴 체크
def check_right(num, direction):
    global gears

    if num != 4:
        # 맨 오른쪽 톱니바퀴는 오른쪽을 체크하지 않음
        if gears[num-1][2] != gears[num][6]:
            # 다른 극인 경우
            if direction == 1:
                # 원래 톱니바퀴가 시계 방향으로 회전
                rotate(-1, gears[num])
            else:
                # 반시계
                rotate(1, gears[num])

# 각 톱니바퀴 점수의 합
def cal_result():
    global gears, result

    for index, val in enumerate(gears):
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

        print(val)
        print(result)


# 초반 값 입력부
gears = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotate_info = [list(map(int, input().split())) for _ in range(k)]  # 회전시킨 톱니바퀴 번호/ 1: 시계, 2: 반시계
result = 0

print(rotate_info)

for i in rotate_info:
    # 회전
    rotate(i[0], i[1])
    # 왼쪽 체크
    check_left(i[0], i[1])
    # 오른쪽 체크
    check_right(i[0], i[1])

cal_result()
print(result)
