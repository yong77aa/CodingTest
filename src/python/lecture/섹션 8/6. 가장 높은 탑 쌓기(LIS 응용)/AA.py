# import sys
# sys.stdin = open("in2.txt")

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0], reverse=True)

    dy = [0] * n
    dy[0] = arr[0][1]

    for i in range(1, n):
        max_dy = 0
        for j in range(i-1, -1, -1):
            if arr[i][2] < arr[j][2] and dy[j] > max_dy:
                max_dy = dy[j]

        dy[i] = max_dy + arr[i][1]

    print(max(dy))