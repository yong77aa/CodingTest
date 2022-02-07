# 세로 N, 가로 M, 1x1
# 빨강, 파랑 구슬 -> 빨강 구슬 빼내기
# 보드의 상태가 주어졌을 때, 최소 빨간 구슬
# 빨간 구슬을 빼내기 위해 움직인 횟수, 10번 이하 및 파란 구슬이 빠지는 경우 -1
# 최단 경로를 찾아야 하는거니까, DFS 보다는 BFS를 사용해서 풀어보자

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]

# 각 구슬 위치 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            red = [i, j]
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = [i, j]

# 벽이 나올 때까지 특정 위치로 계속 이동하면서 탐색함
def movemove(x, y, dx, dy):
    move = 0
    while graph[x+dx][y+dy] != '#':
        if graph[x+dx][y+dy] == 'O':  # 구멍에 빠진 경우
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    return x, y, move


def bfs():
    # 빨간 구슬과 파란 구슬 동시에 방문체크 해야함
    visit = {}
    queue = deque([red + blue])
    visit[red[0], red[1], blue[0], blue[1]] = 0
    while queue:
        rx, ry, bx, by = queue.popleft()  # 공의 위치를 하나 꺼내서 그 위치를 기준으로 다시 이동함
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 상, 하, 좌, 우
            nrx, nry, rmove = movemove(rx, ry, dx, dy)
            nbx, nby, bmove = movemove(bx, by, dx, dy)

            # 두 공 모두 또는 파란 공만 탈출한 경우
            if not nbx and not nby:
                continue

            # 빨간 공만 탈출한 경우
            elif not nrx and not nry:
                print(visit[rx, ry, bx, by] + 1)
                return

            # 두 공이 같은 위치에 있는 경우
            elif nrx == nbx and nry == nby:
                # 이동거리가 적은 구슬을 한 칸 뒤로
                if rmove > bmove:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 해당 위치가 방문된 것이 아니면, 방문 된 것으로 저장
            if (nrx, nry, nbx, nby) not in visit:
                visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by] + 1  # 지금까지 움직였던 횟수에 +1 해서 저장함
                queue.append([nrx, nry, nbx, nby])  # 구슬들의 위치를 저장

        # answer에 값을 넣었거나 queue가 비었거나 움직인 횟수가 10이상이면 그만
        if not queue or visit[rx, ry, bx, by] >= 10:
            print(-1)
            return


bfs()