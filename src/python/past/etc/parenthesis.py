def main():
    num = int(input())

    for i in range(num):
        text = input()
        left = 0
        right = 0

        if len(text) % 2 != 0:  # 문자가 짝수개가 아니면 쌍을 이루지 않은 것임
            print("NO")

        else:
            for temp in text:  # 문자를 하나씩 확인
                # 각 종류마다 카운트를 하나씩 추가
                if temp == "(":
                    left += 1
                else:
                    right += 1

            if left != right:  # 카운트가 같지 않으면 쌍을 이루지 않음
                print("NO")
            else:  # 카운트가 같으면 쌍을 이룸
                print("YES")


if __name__ == '__main__':
    main()