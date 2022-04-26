# 소수 출력

def main():
    num = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    for i in numbers:
        error = 0
        if i != 1:
            for j in range(2, i):
                if i % j == 0:  # 나눈 몫이 0 이면 소수가 아니라는 뜻임
                    error += 1
            if error == 0:
                result +=1

    print(result)


if __name__ == "__main__":
    main()