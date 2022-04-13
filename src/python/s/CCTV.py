# 모든 경우의 수를 구해야 하기 때문에 DFS로 접근
# DFS + 백드래킹 방식으로 해결
import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

cctv = []  # cctv의 위치 및 종류를 저장하기 위한 배열
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j]])  # cctv 위치 및 종류

# 이동 방향 (북, 동, 남, 서)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# cctv 종류에 따른 감시 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


# cctv 감시 (한 방향의 벽까지)
def watch(x, y, direction, tmp):
    for i in direction:
        nx, ny = x, y

        while True:
            # 이동할 수 없을 때까지
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or tmp[nx][ny] == 6:
                # 이동 불가능한 경우
                break
            elif tmp[nx][ny] == 0:
                # 빈 칸이면 감시한 것으로 변경
                tmp[nx][ny] = '#'


# dfs 구현
def dfs(n, office):
    global result

    temp = copy.deepcopy(office)
    if n == len(cctv):
        # 모든 종류의 cctv를 확인한 경우
        blank = 0  # 빈 칸 개수
        for t in temp:
            blank += t.count(0)  # 사각지대 개수
        result = min(result, blank)
        return

    x, y, t = cctv[n]
    # 감시 구역 계산
    for d in direction[t]:
        watch(x, y, d, temp)
        dfs(n + 1, temp)
        temp = copy.deepcopy(office)


result = 1e9
dfs(0, office)
print(result)
