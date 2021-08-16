# 약수를 구함
# 두번째로 입력하는 숫자는 (input)번째로 작은 약수를 말함

def main():
    p, q = list(map(int, input().split()))
    divisors = []

    for i in range(1, p+1):
        temp = p % i  # 나머지
        if temp == 0:  # 나머지가 0 이라 해당 숫자의 몫인 경우
            num = p / i
            divisors.append(int(num))  # 리스트에 몫을 넣음

    divisors = list(set(divisors))  # 자료형을 set 으로 바꿔서 중복을 제거하고 정렬함

    if len(divisors) < q:
        print(0)
    else:
        print(divisors[q-1])

if __name__ == "__main__":
    main()