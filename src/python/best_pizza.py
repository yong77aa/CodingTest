# 열랑이 최고가 되는 피자를 선택함
# 같은 토핑은 2개 이상 안됨
# 토핑을 하나도 안올려도 됨
# 도우는 A, 토핑은 모두 B 실제 피자는 A + B
# 최고의 피자의 1달러 당 열량의 수

def main():
    topping_type = int(input())  # 토핑 종류
    a, b = list(map(int, input().split()))  # 도우, 토핑 비용
    dough = int(input())
    kcals = []

    kcal = 0
    cost = 0
    result = 0

    for i in range(topping_type):
        kcals.append(int(input()))

    kcals.sort(reverse=True)

    for i in kcals:
        kcal += i  # 칼로리 증가
        cost += b  # 토핑 가격 하나씩 증가

        cal = (dough + kcal) / float(a + cost)  # 최고의 피자의 1달러 당 열량의 수

        if result > cal:
            break
        else:
            result = cal

    print(int(result))

if __name__ == "__main__":
    main()