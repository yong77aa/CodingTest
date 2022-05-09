# 당장 가장 큰 가치를 가진 동전으로 나누면 됨
# 탐욕법 기초

n, k = map(int, input().split())
coinList = []
result = 0

for i in range(n):
    temp = int(input())
    coinList.append(temp)

coinList.sort(reverse=True)

for i in coinList:
    if not k < i:
        share = k // i
        k -= share * i
        result += share

print(result)