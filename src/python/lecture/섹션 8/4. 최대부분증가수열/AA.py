import sys
sys.stdin = open("in1.txt", "r")

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    answer = 0

    dy = [0] * (n+1)
    dy[1] = 1

    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1):
            if arr[j] < arr[i] and dy[j] > max:
                max = dy[j]
        dy[i] = max + 1

        if dy[i] > answer:
            answer = dy[i]

    print(answer)