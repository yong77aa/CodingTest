# 모든 팀의 경우의 수를 탐색해야 하니까 dfs
def dfs(depth, idx):
    global diff

    if depth == n/2:
        # 짝수만 들어옴
        power1, power2 = 0, 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    # i와 j가 같으면 값이 0이니까 종료
                    continue
                elif visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]

        diff = min(diff, abs(power1 - power2))  # 최소값 선택
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True  # 팀 하나를 기준으로 다른 경우의 수로 비교해나감 -> 0,1 선택하고 다른거 비교
            print(visited)
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
diff = int(1e9)

dfs(0, 0)
print(diff)