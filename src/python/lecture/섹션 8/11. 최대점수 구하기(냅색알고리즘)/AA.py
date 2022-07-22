import sys
sys.stdin = open("in1.txt")

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dy = [0] * (m+1)

    for i in arr:
        score, time = i[0], i[1]
        for j in range(m, time-1, -1):
            dy[j] = max(dy[j], score + dy[j-time])

    print(dy[m])
