# 세로: N, 가로: M
# 주사위 놓은 곳 좌표: x, y
# 명령의 개수: K
n, m, x, y, k = map(int, input.split())
arr = [list(map(int, input().split()) for _ in range(n))]  # 지도
move = list(map(int, input().split()))  # 이동하는 명령
dice = [0, 0, 0, 0, 0, 0]  # 주사위

# 방향 저장 동, 서, 북, 남
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(k):
    direction = move[i] - 1  # 이동하는 방향
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= m:
        # 위치가 맵의 밖으로 나가는 경우
        # 원래 위치로 원상복귀 후 아무것도 하지 않음
        x -= dx[direction]
        y -= dy[direction]
        continue

    if direction == 0:
        # 동쪽으로 이동

    elif direction == 1:
        # 서쪽으로 이동

    elif direction == 2:
        # 북쪽으로 이동

    else:
        # 남쪽으로 이동