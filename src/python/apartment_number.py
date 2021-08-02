a = int(input())
graph = []
visited = []

for i in range(a):
    graph.append(list(map(int, input())))
    visited.append([0] * a)

def dfs(i, j):
    global count

    if i >= a or i < 0 or j >= a or j < 0:  # 리스트의 바깥쪽에 접근하면 종료
        return False

    if graph[i][j] == 0:  # 해당 값이 0 이면 종료
        return False

    graph[i][j] = 0  # 해당 노드의 값이 1이면 0 으로 바꿈
    count += 1  # count 증가

    # 각 방향마다 재귀호출 함
    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i-1, j)
    dfs(i, j-1)

    return True