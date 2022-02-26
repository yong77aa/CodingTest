n, m = map(int, input().split())  # 세로 N, 가로 M
arr = [list(map(int, input().split())) for _ in range(n)]  # 보드 저장
visited = [[0] * m for _ in range(n)]  # 방문 여부

max = max(map(max, arr))  # 해당 보드의 최대값

result = 0
x, y = 0, 0

# 동, 서, 북, 남 이동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방향 탐색 및 값 이동부
def search(a, b, idx, total):
    global max_value

    if idx == 3:
        # 계산을 끝낸 경우
        return

# 실제 계산