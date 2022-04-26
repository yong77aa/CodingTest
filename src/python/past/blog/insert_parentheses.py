# () = 2
# [] = 3
# 안에 포함되어 있으면 곱하기
# 괄호열을 읽고 괄호값 계산해 출력
# 올바르지 못하면 0

import sys

# 완벽환 괄호인지 확인하는 메서드
def check(words):
    open_2_count = 0  # 열린 ( 괄호의 개수
    close_2_count = 0  # 닫힌 ( 괄호의 개수
    open_3_count = 0  # 열린 [ 괄호의 개수
    close_3_count = 0  # 닫힌 ] 괄호의 개수

    for i in words:
        if i == '(':  # 열린 ( 괄호인 경우
            open_2_count += 1
        elif i == ')':  # 닫힌 ) 괄호인 경우
            close_2_count += 1
        elif i == '[':  # 열린 [ 괄호인 경우
            open_3_count += 1
        elif i == ']':  # 닫힌 ] 괄호인 경우
            close_3_count += 1

    if open_2_count == close_2_count and open_3_count == close_3_count:  # 열린 괄호와 닫힌 괄호의 개수가 같으면 완벽한 괄호
        return True
    elif words:
        return False
    else:
        return False

if __name__ == "__main__":
    words = input()  # 최초에 입력하는 괄호
    temp_list = []

    if check(words):  # 완벽한 괄호인 경우
        temp = 0
        for i in words:
            # 여는 괄호의 경우에는 스택에 넣음
            if i == '(':
                temp_list.append(i)
            elif i == '[':
                temp_list.append(i)
            # 닫는 괄호의 경우에는 가장 위의 값을 꺼내서 계산
            elif i == ')':
                temp = 2
                while True:
                    top = temp_list.pop()  # 가장 위에 있는 값을 꺼내서
                    if type(top) == int:  # 기존에 있던 값이 숫자인 경우에는
                        temp = temp * top  # 괄호 안에 있는 숫자를 의미하니까 곱함
                    elif top == '(':  # 여는 괄호가 나온 경우에는
                        temp_list.append(temp)  # 그냥 2를 리스트에 넣음 (닫는 기호가 나온거니까 기존의 여는 기호는 넣을 필요없음)
                        break
            # ) 괄호와 똑같은 방식으로 연산함
            elif i == ']':
                temp = 3
                while True:
                    top = temp_list.pop()
                    if type(top) == int:
                        temp = temp * top
                    elif top == '[':
                        temp_list.append(temp)
                        break

            temp2 = 0  # 괄호 간의 연산을 하기 위한 변수
            while temp_list:
                top = temp_list.pop()
                if type(top) == int:  # 맨 위에 있는 값이 숫자인 경우
                    temp2 += top  # 괄호 안에 있는 것이 아니니까 그냥 더함
                else:  # 괄호인 경우
                    temp_list.append(top)  # 다시 리스트에 넣음
                    break

            if temp2:
                temp_list.append(temp2)

        print(temp_list[-1])

    else:  # 완벽하지 않은 괄호인 경우
        print(0)
