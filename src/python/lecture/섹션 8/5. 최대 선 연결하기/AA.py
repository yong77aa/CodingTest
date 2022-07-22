# import sys
# sys.stdin = open("in1.txt", "r")

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    dy = [0] * n
    dy[0] = 1

    for i in range(1, n):
        max_temp = 0
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i] and max_temp < dy[j]:
                max_temp = dy[j]

        dy[i] = max_temp + 1

    print(max(dy))
