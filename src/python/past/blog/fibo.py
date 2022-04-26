#  피보나치 수열 출력
#  N 번째 출력
#  Fn = Fn-1 + Fn-2


def main():
    n = int(input())
    first, second = 0, 1
    fibo_list = []
    fibo_list.append(first)
    fibo_list.append(second)

    for i in range(2, n+1):
        temp = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(temp)

    print(fibo_list[n])

if __name__ == "__main__":
    main()

