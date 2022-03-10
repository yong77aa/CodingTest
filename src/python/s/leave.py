n = int(input())  # 남은 일수 N
t, p = [], []  # 상담을 완료하는데 걸리는 기간 t, 금액 p

for _ in range(n):
    T, P = map(int, input().split())
    t.append(t)
    p.append(p)

d = [0] * (n+1)

for i in range(n - 1, -1, -1):
    if i + T[i] > n:
        # i일에 상담하는 것이 퇴사일을 넘기면 상담 X
        d[i] = d[i+1]
    else:
        # 상담을 하는것과 안하는 것 중 선택
        d[i] = max(d[i+1], p[i] + d[i + T[i])

print(d[0])
