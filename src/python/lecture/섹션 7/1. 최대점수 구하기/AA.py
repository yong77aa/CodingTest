# import sys
# sys.stdin = open("in2.txt", "rt")


def dfs(index, sum, time):
    global answer
    if time > m:
        return

    if index == n:
        if sum > answer:
            answer = sum
    else:
        dfs(index+1, sum+arr[index][0], time+arr[index][1])
        dfs(index+1, sum, time)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = -1e9
    dfs(0, 0, 0)
    print(answer)
