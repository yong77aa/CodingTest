import sys
sys.stdin = open("in1.txt")

if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dy = [0] * (n+1)

    for i in range(n):
        w, v = arr[i][0], arr[i][1]
        # w: 보석의 무게, v: 보석의 가치
        for j in range(w, target+1):
            # j-w는 남은 위치에 넣을 수 있는 가치를 더해주기 위함임
            # 8자리에 5짜리를 넣는다고 치면 3짜리를 추가로 더 넣을 수 있으니까 그걸 더해주는거임
            dy[j] = max(dy[j], dy[j-w]+v)

    print(dy[target])


