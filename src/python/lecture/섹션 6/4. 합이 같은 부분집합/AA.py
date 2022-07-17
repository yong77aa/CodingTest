import sys
sys.stdin=open("in1.txt", "r")


def DFS(v, s):
    if v == n:
        if s == (arr_sum - s):
            print("YES")
            sys.exit(0)
    else:
        DFS(v+1, s + arr[v])
        DFS(v+1, s)


if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr_sum = sum(arr)

    DFS(0, 0)
    print("NO")

    