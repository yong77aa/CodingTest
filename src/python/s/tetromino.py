n, m = map(int, input().split())  # 세로 N, 가로 M
arr = [list(map(int, input().split())) for _ in range(n)]  # 보드 저장
max_value = max(map(max, arr))  # 해당 보드의 최대값
visited = [[0] * m for _ in range(n)]  # 방문 여부
result = 0  # 결과 값

# 동, 서, 북, 남 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방향 탐색 및 값 이동부
def dfs(x, y, idx, total):
    global result

    if result > total + max_value * (3 - idx):
        # 해당 노드의 최댓값인 경우 더 반복하지 않음
        return

    if idx == 3:
        # 계산을 끝낸 경우
        result = max(result, total)
        return
    else:
        for i in range(4):
            # 좌표 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # 이동한 위치가 보드 안에 있고, 방문하지 않은 노드인 경우
                visited[nx][ny] = 1  # 해당 노드를 방문한 것으로 수정

                if idx == 1:
                    # 두번째 이동인 경우 (ㅗ) 모양
                    # 한번만 더 이동하면 되니까 한번 호출함
                    dfs(x, y, idx + 1, total + arr[nx][ny])

                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visited[nx][ny] = 0  # 반복해서 탐색한 이후 해당 노드를 방문하지 않은 것으로 수정


for i in range(n):
    for j in range(m):
        visited[i][j] = 1  # 해당 노드를 방문한 것으로 수정
        dfs(i, j, 0, arr[i][j])  # 모든 노드를 계산
        visited[i][j] = 0

print(result)