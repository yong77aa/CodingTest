import sys
sys.stdin = open("in1.txt", "r")


def DFS(depth, sum):
    global n, target, answer
    if sum > target:
        # 총 합이 target을 넘는 경우 종료
        return
    if depth > answer:
        # 기존에 수행했던 최적보다 더 많이 수행하는 경우 종료
        return

    if sum == target:
        if depth < answer:
            # 최적값 저장
            answer = depth
    else:
        for i in range(n):
            DFS(depth+1, sum+coin_type[i])


if __name__ == "__main__":
    n = int(input())
    coin_type = list(map(int, input().split()))
    coin_type.sort(reverse=True)
    target = int(input())
    answer = 1e49

    DFS(0, 0)
    print(answer)
