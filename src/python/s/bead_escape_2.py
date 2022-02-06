# 세로 N, 가로 M, 1x1
# 빨강, 파랑 구슬 -> 빨강 구슬 빼내기
# 보드의 상태가 주어졌을 때, 최소 빨간 구슬
# 빨간 구슬을 빼내기 위해 움직인 횟수, 10번 이하 및 파란 구슬이 빠지는 경우 -1

from sys import stdin

n, m = map(int, input.split())
graph = [list(stdin.readlin()) for _ in range(n)]

#  구슬의 위치를 찾아서 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':  # 빨강
            graph[i][j] = '.'
            red = [i][j]
        elif graph[i][j] == 'B':  # 파랑
            graph[i][j] = '.'
            blue = [i][j]  # 위치 저장

#  구슬 움직여 위치 반환
def move(x, y, dx, dy):
    move = 0
    while graph[x+dx][y+dy] != '#':  # 벽에 걸리지 않을 때까지
        if graph[x+dx][y+dy] == '0':  # 구멍
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    return x, y, move

#  결과를 찾을 때까지 계속 움직임
