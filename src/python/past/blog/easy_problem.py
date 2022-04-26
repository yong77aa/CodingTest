# 1 2 2 3 3 3 ... 같은 식으로 증가
# 일정한 구간에서 구간의 합 구하기

def main():
    x, y = list(map(int, input().split()))
    numbers = []
    endLoopFlag = False

    for i in range(y+1):
        for j in range(i):
            if len(numbers) == y:
                endLoopFlag = True
                break
            numbers.append(i)

        if endLoopFlag == True:
            break

    print(sum(numbers[x-1:y]))

if __name__ == "__main__":
    main()