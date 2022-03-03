from collections import deque

n = int(input())  # 보드의 크기
m = int(input())  # 사과의 개수
arr = [[0] * n for _ in range(n)]  # 게임 보드 생성

# 보드 위에 사과의 위치 저장
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1

k = int(input())  # 방향 전환 횟수
change = {}  # 방향 전환 정보 {x초 뒤, (좌, 우)}

# 방향 전환 정보 저장
for _ in range(k):
    time, direction = map(str, input().split())
    change[int(time)] = direction

# 북: 0, 동: 1, 남: 2, 북: 3
# 방향 전환 함수
def direction_change(c):
    global now_direction
    if c == 'L':
        # 왼쪽 회전
        if now_direction == 0:
            now_direction = 3
        else:
            now_direction -= 1
    else:
        # 오른쪽 회전
        if now_direction == 3:
            now_direction = 0
        else:
            now_direction += 1

snake = deque([[0, 0]])  # 최초 뱀의 위치

# 방향 저장 '북, 동, 남, 서' 순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

now_direction = 1  # 시작 방향 동쪽
time = 0  # 게임 진행 시간
x, y = 0, 0  # 뱀의 머리 위치

while True:
    time += 1
    x += dx[now_direction]
    y += dy[now_direction]

    if time in change.keys():
        direction_change(change[time])  # 방향 전환

    if 0 <= x and x < n and 0 <= y and y < n:
        # 게임판 범위 안
        if [x, y] in snake:
            # 몸에 부딪힌 경우
            break

        if arr[x][y] == 1:
            # 사과가 있는 경우
            arr[x][y] = 0  # 해당 위치의 사과의 값을 0으로 변경
            snake.append([x, y])

        elif arr[x][y] == 0:
            # 사과가 없는 경우
            snake.append([x, y])
            snake.popleft()

    else:
        # 게임판 범위 밖
        break

print(time)
