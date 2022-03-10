n = int(input())  # 남은 일수 N
t, p = [], []  # 상담을 완료하는데 걸리는 기간 t, 금액 p

for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

d = [0] * (n+1)

for i in range(n - 1, -1, -1):
    if i + t[i] > n:
        # i일에 상담하는 것이 퇴사일을 넘기면 상담 X
        d[i] = d[i+1]
    else:
        # d[i+1]: 상담을 하지 않고 이전 반복의 결과를 그대로 가져옴
        # d[i + t[i]]: 해당 일의 보수 + 해당 일이 끝난 날의 최대 보수
        # 두개를 비교해서 상담을 하는게 이득인지 아닌게 이득인지를 계산함
        d[i] = max(d[i+1], p[i] + d[i + t[i]])

print(d[0])
