# 하나씩 탐색하는 BFS로 풀어보자
# 한 그래프로 계속 탐색해 나가니까 깊은 복사는 할 필요 없음

n, m = map(int, input().split())  # 세로: n, 가로: m
r, c, d = map(int, input().split())  # 좌표: (r, c), 바라보는 방향: d (0: 북, 1: 동, 2: 남, 3: 서)
arr = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[0] * m for _ in range(n)]  # 청소한 지역 저장
cleaned[r][c] = 1
result = 1
turn_time = 0  # 회전 횟수

# 방향 이동 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환
def change_direction():
    global d
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    else:
        d = 2


# 청소기 이동
while True:
    change_direction()  # 청소한 뒤 왼쪽으로 방향 전환

    # 전환한 방향으로 좌표 이동
    mx = r + dx[d]
    my = c + dy[d]

    if cleaned[mx][my] == 0 and arr[mx][my] == 0:
        # 청소하지 않은 공간인 경우
        r, c = mx, my  # 1칸 전진
        cleaned[mx][my] = 1  # 청소
        result += 1
        turn_time = 0  # 회전 횟수 초기화

    else:
        # 이동이 불가능 한 경우, 회전 및 회전 횟수 증가
        turn_time += 1

    if turn_time == 4:
        # 네 방향 모두 청소가 되어있거나 벽인 경우
        # 한 칸 뒤로 이동 (한칸 이동해놨던 좌표 원상복귀 및 뒤로 한칸 더)
        mx = r - dx[d]
        my = c - dy[d]

        if arr[mx][my] == 0:
            # 이동할 수 있으면 이동
            r, c = mx, my

        else:
            break

        turn_time = 0  # 이동 횟수 초기화

print(result)