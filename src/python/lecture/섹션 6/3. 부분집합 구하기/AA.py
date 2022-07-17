import sys


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if visited[i] == 1:
                print(i, end=" ")
    else:
        visited[v] = 1
        DFS(v+1)
        visited[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    sys.stdin = open("in1.txt", "r")
    n = int(input())
    visited = [0] * n

    DFS(n)


