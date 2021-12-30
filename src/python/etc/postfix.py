def main():
    str = input()
    stack = []
    res = ''

    for s in str:
        if s.isalpha():
            res += s
        else:
            if s == '(':  # 시작 괄호
                stack.append(s)
            elif s == '*' or s == '/':  # 우선순위가 높은 연산자
                while stack and (stack[-1] == '*' or stack[-1] == '/'):  # 이 연산자가 스택의 끝에 있는 경우
                    #  + - 보다 우선순위가 높으니까 그냥 pop한다
                    res += stack.pop()  # 결과에 누적
                stack.append(s)  # 없으면 그냥 스택에 누적
            elif s == '+' or s == '-':  # 우선순위가 낮은 연산자
                while stack and (stack[-1] != '('):  # 시작 괄호가 나올때까지
                    #  + - 는 우선순위가 가장 낮으니까 기존에 있던걸 전부 pop 해도 됨
                    res += stack.pop()  # 결과에 누적
                stack.append(s)  # 없으면 그냥 스택에 누적
            elif s == ')':  # 종료 괄호
                while stack and (stack[-1] != '('):  # 시작 괄호가 나올때까지
                    # 시작 괄호가 나올때까지 누적하는 이유는 괄호 안에 있는 연산자가 우선이기 때문
                    res += stack.pop()  # 누적함
                stack.pop()

    while stack:
        res += stack.pop()  # 스택에 남아있는 연산자 저장

    print(res)

if __name__ == "__main__":
    main()