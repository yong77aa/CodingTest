# 안보고 코딩해보기

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(j):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j]])  # cctv 위치, 종류 저장

# 이동방향 (북, 동, 남, 서)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

