# 첫번째 줄에는 테스트 케이스의 개수
# 이진수로 나타냈을 때 1의 위치를 출력
# 1의 위치를 공백으로 구분해서 줄 하나에 출력

import math

def main():
    num = int(input())
    test_case = []

    for i in range(num):
        temp = int(input())
        test_case.append(temp)  # 하나씩 입력받아서 리스트에 저장

    for i in test_case:
        binary = []
        while True:
            value = i % 2
            i = math.floor(i / 2)
            binary.append(value)  # 작은 숫자부터 출력해야 하니 굳이 돌릴 필요 없음

            if i == 0:
                break

        for idx, val in enumerate(binary):
            if val == 1:
                print(idx, end=' ')
        print()

if __name__ == "__main__":
    main()