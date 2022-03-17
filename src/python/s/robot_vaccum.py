# 하나씩 탐색하는 BFS로 풀어보자
# 한 그래프로 계속 탐색해 나가니까 깊은 복사는 할 필요 없음

n, m = map(int, input().split())  # 세로: n, 가로: m
r, c, d = map(int, input().split())  # 좌표: (r, c), 바라보는 방향: d (0: 북, 1: 동, 2: 남, 3: 서)
arr = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[0] * m for _ in range(n)]  # 청소한 지역 저장
result = 0

# 방향 이동 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환
def change_direction(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2


# 청소기 이동
while True:
    if cleaned[r][c] == 0:
        # 청소되지 않은 지역인 경우
        cleaned[r][c] = 1  # 현재 위치 청소
        result += 1

    d = change_direction(d)  # 청소한 뒤 왼쪽으로 방향 전환

    # 전환한 방향으로 좌표 이동
    mx = r + dx[d]
    my = c + dy[d]

    if cleaned[mx][my] == 0 and arr[mx][my] != 1:
        # 벽이 아니고, 청소하지 않은 공간인 경우
        r, c = mx, my  # 1칸 전진
        cleaned[mx][my] = 1  # 청소
        result += 1

    elif cleaned[mx][my] == 1 or arr[mx][my] == 1:
        # 청소할 공간이 없고, 벽이 아닌 경우
        # 왼쪽 방향으로 회전
        d = change_direction(d)

    elif (cleaned[r+dx[0]][c+dy[0]] == 1 and cleaned[r+dx[1]][c+dy[1]] == 1 and cleaned[r+dx[2]][c+dy[2]] == 1 and cleaned[r+dx[3]][c+dy[3]] == 1) or (arr[r+dx[0]][c+dy[0]] == 1 and arr[r+dx[0]][c+dy[0]] == 1 and arr[r+dx[0]][c+dy[0]] == 1 and arr[r+dx[0]][c+dy[0]] == 1):
        # 네 방향 모두 청소가 되어있거나 벽인 경우
        # 한 칸 뒤로 이동
        mx = r - dx[d]
        my = c - dy[d]

        if arr[mx][my] == 1 or mx < 0 or my < 0:
            # 뒤쪽 방향이 벽이라 후진도 할 수 없으면
            break

print(result)