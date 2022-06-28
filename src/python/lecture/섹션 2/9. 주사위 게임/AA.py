import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())
result = 0

for i in range(n):
    temp = input().split()
    temp.sort()
    a, b, c = map(int, temp)

    if a==b and b==c:
        # 모두 같은 경우
        money = 10000 + (a*1000)
    elif a==b or a==c or b==c:
        # 두개만 같은 경우
        if a==b or a==c:
            money = 1000 + (a*100)
        elif b==c:
            money = 1000 + (b*100)
    else:
        # 다 다른 경우
        money = c*100

    if money > result:
        result = money

print(result)