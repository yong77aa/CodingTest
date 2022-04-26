# 최솟값과 최댓값 구하기
# 첫째줄에 정수의 개수
# 둘째줄에 N개의 정수 공백 구분


def main():
    n = int(input())
    items = list(map(int, input().split()))

    print(str(min(items)) + " " + str(max(items)))


if __name__ == "__main__":
    main()