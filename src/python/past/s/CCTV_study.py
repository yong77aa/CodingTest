# 안보고 코딩해보기
import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j]])  # cctv 위치, 종류 저장

# 이동방향 (북, 동, 남, 서)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# CCTV 감시방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 4]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


# cctv 감시
def watch(x, y, direction, arr):
    # 애초에 CCTV 방향이 다 들어가 있으니까 반복문으로 모든 경우를 따짐
    for i in direction:
        mx, my = x, y
        while True:
            mx += dx[i]
            my += dy[i]
            if mx >= n or my >= m or mx < 0 or my < 0 or arr[mx][my] == 6:
                break
            elif arr[mx][my] == 0:
                arr[mx][my] = "#"  # 감시완료


def dfs(n, office):
    global result
    temp = copy.deepcopy(office)
    if n == len(cctv):
        blank = 0
        for i in temp:
            blank += i.count(0)
        result = min(result, blank)
        return

    x, y, t = cctv[n]

    for d in direction[t]:
        watch(x, y, d, temp)
        print(temp)
        dfs(n+1, temp)
        # temp = copy.deepcopy(office)


result = 1e9
dfs(0, office)
print(result)