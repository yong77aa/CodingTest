def main():
    num, target = map(int, input().split())
    value = []
    count = 0

    for i in range(num):
        temp = input()
        value.append(temp)  # 동전의 가치를 리스트에 하나씩 넣음

    for i in reversed(value):  # 리스트를 역순으로 가장 큰 가치부터 시작해서
        temp = target // int(i)  # 해당 값에서 가장 큰 가치를 나눔
        target -= temp * int(i)  # 목표 값은 나눈 몫에서 빼서 계속 줄여나가야함
        count += temp  # 몫이 해당 동전의 개수니까 count에 누적

    print(count)

if __name__ == "__main__":
    main()