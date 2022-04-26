# 세로: N, 가로: M
# 주사위 놓은 곳 좌표: x, y
# 명령의 개수: K
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))  # 이동하는 명령
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # 주사위

# 방향 저장 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    direction = move[i] - 1  # 이동하는 방향
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not 0 <= nx < n or not 0 <= ny < m:
        # 위치가 맵의 밖으로 나가는 경우
        # 원래 위치로 원상복귀 후 아무것도 하지 않음
        continue

    x, y = nx, ny

    # 주사위 이동
    if direction == 0:
        # 동
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 1:
        # 서
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 2:
        # 북
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif direction == 3:
        # 남
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    if arr[x][y] != 0:
        # 이동한 칸에 쓰여있는 수가 0이 아님
        dice[6] = arr[x][y]  # 칸에 쓰여있는 수가 주사위 바닥면으로 복사
        arr[x][y] = 0  # 칸의 수는 0
    else:
        # 이동한 칸에 쓰여있는 수가 0
        arr[x][y] = dice[6]  # 주사위 바닥면의 수가 칸에 복사

    print(dice[1])

