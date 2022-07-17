import sys
sys.stdin=open("in1.txt", "r")


def DFS(v, s):
    global answer
    if s > c:
        return

    if v == n:
        if s > answer:
            answer = s
    else:
        DFS(v+1, s + arr[v])
        DFS(v+1, s)

if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = []
    for i in range(n):
        temp = int(input())
        arr.append(temp)

    answer = 0
    DFS(0, 0)

    print(answer)