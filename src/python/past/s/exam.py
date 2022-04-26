import math

n = int(input())  # 시험장 개수
a = list(map(int, input().split()))  # 응시자의 수
b, c = map(int, input().split())  # 총 감독관, 부 감독관

# 각 시험장에서 각각 총 감독관이 감시할 수 있는 수험생의 숫자를 뺌
for i in range(n):
    if a[i] - b > 0:
        a[i] -= b
    else:
        a[i] = 0

result = n  # 기본적으로 한개 시험장에 총 감독관이 한명씩은 있어야함

for i in range(n):
    if a[i] <= 0:
        continue
    else:
        temp = int(math.ceil(a[i] / c))

    result += int(temp)

print(result)
