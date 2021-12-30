from collections import deque

def main():
    a, b = map(int, input().split())
    my_list = list(map(int, input().split()))

    queue = deque(range(1, a + 1))
    cnt = 0
    for n in my_list:
        while queue[0] != n:
            t = queue.index(n)
            if t <= len(queue) - t - 1:  # 해당 값이 왼쪽에 있으면
                queue.append(queue.popleft())  # 왼쪽에서 뽑은걸 오른쪽으로 붙임
            else:  # 오른쪽에 있으면 0
                queue.appendleft(queue.pop())  # 오른쪽에서 뽑음
            cnt += 1  # 연산의 갯수 증가
        queue.popleft()  # 첫번째 원소를 뽑아냄
    print(cnt)

if __name__ == '__main__':
    main()
