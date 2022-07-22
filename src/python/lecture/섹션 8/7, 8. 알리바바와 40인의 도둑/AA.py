# import sys
# sys.stdin = open("in1.txt")

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]

    # 첫번째 행, 열에는 선택하지 않고 누적한 값 저장
    for i in range(n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]

    # 그 이후부터는 최적 값 선택하여 계산
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]

    print(dy[n-1][n-1])