# 숫자가 두개 주어질 때 M이상 N이하의 자연수 중 소수인 것을 골라 소수의 합과 최솟값

def main():
    n = int(input())
    m = int(input())
    sosu_list = []

    for i in range(n, m+1):
        is_sosu = True
        if i != 1:
            for j in range(2, i):
                if i % j == 0:
                    is_sosu = False
                    break

            if is_sosu == True:
                sosu_list.append(i)

    if len(sosu_list) == 0:
        print(-1)
    else:
        print(sum(sosu_list))
        print(min(sosu_list))

if __name__ == "__main__":
    main()