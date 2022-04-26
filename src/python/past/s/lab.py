import copy
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 방향 저장 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global result
    q = deque()
    temp = copy.deepcopy(arr)  # 원래 그래프를 다시 또 써야하니까 깊은 복사함
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))  # 감염된 지역을 큐에 저장해서 bfs 실행

    while q:
        # 감염된 지역을 하나씩 순회하면서 4방위를 모두 감염시킴
        x, y = q.popleft()

        for i in range(4):
            # 4방위 반복 실행
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 그래프의 범위 안에서만 실행
                if temp[nx][ny] == 0:
                    # 감염되지 않은 지역인 경우
                    temp[nx][ny] = 2
                    q.append([nx, ny])

    count = 0
    for i in temp:
        count += i.count(0)
    result = max(result, count)  # 최대 값 저장


def wall(x):
    if x == 3:
        # 벽을 이미 세운 경우 그때서 탐색 실행
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                # 아무것도 없는 지역을 대상으로
                # 모든 경우의 수에 벽을 세워서 탐색함
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0  # 원상태로 복귀


wall(0)
print(result)
