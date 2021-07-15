from collections import deque

def main():
    num = int(input())

    deque1 = deque() # 빈 큐 만들기

    for i in range(1, num+1):
        deque1.append(i) # 1부터 N까지를 큐에 넣음

    while(True):
        deque1.popleft() # 제일 위에 있는 카드를 바닥에 버린다
        num = deque1.popleft() # 그 다음 제일 위에 있는 카드를 빼고
        deque1.append(num) # 제일 아래에 있는 카드 밑으로 옮긴다

        if(len(deque1) == 1): # 한개만 남았을 때 반복문 종료
            break

    print(deque1.pop()) # 남은 한개 출력


if __name__ == '__main__':
    main()
