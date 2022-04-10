# 모든 경우의 수를 구해야 하기 때문에 DFS로 접근
# DFS + 백드래킹 방식으로 해결

n, m = map(int, input().split())
office = [list(map(int, input.split())) for _ in range(n)]

# 이동 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# cctv 종류에 따른 감시 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    5: [[0, 1, 2, 3]]
}

# cctv 감시 (한 방향의 벽까지)
def watch(x, y, cctv, tmp):
    for i in direction:
        nx, ny = x, y,
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0:  # 빈 칸이면 감시한 것으로 변경
                tmp[nx][ny] = '#'

# dfs 구현
def dfs(n, office):
