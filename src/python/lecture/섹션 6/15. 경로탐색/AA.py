import sys
sys.stdin = open("in1.txt", "rt")


def DFS(v):
    global result
    if v == n:
        result += 1
    else:
        for i in range(1, n+1):
            if arr[v][i] == 1 and ch[i] == 0:
                # 갈 수 있고 방문하지 않은 노드
                ch[i] = 1  # 해당 노드 방문처리
                DFS(i)  # 깊이 탐색
                ch[i] = 0  # 방문처리 했던 노드 초기화


if __name__ == "__main__":
    n, m = map(int, input().split())

    # 모든 경우의 수를 저장하기 위한 2차원 배열 선언
    arr = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1

    print(arr)

    ch = [0] * (n+1)  # 노드 방문 여부
    result = 0  # 결과
    ch[1] = 1  # 첫번째 노드는 무조껀 가니까 방문처리
    DFS(1)  # 탐색 수행
    print(result)