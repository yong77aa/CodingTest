a = int(input())

graph = []
visited = []
count = 0
result = []

# 이동하기 위한 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(a):
    graph.append(list(map(int, input())))
    visited.append([0] * a)

def dfs(i, j):
    global count

    if i >= a or i < 0 or j >= a or j < 0:  # 리스트의 바깥쪽에 접근하면 종료
        return False

    if graph[i][j] == 1:
        count += 1  # 카운트 해준 뒤에
        graph[i][j] = 0  # 해당 노드는 방문한 것으로 수정

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            dfs(nx, ny)
        return True


for i in range(a):
    for j in range(a):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
for i in result:
    print(i)