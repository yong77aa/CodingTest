# 같은 값을 만나면 합쳐짐
# 5번을 움직여서 가장 큰 수 (전체가 다 움직임)

# 상, 하, 좌, 우 모든 경우의 수를 확인해야 하므로 DFS가 적합할 것 같음
# 이동하려는 위치의 숫자 기준
# 1. 0이면 해당 숫자를 0 위치로 이동
# 2. 자신과 같으면 앞의 숫자를 2배
# 3. 자신과 다르면 인덱스를 하나 늘리고 그 자리에 배치
import copy
from sys import stdin

size = int(stdin.readline())
# 현재 보드의 상태 저장
board = [list(map(int, stdin.readline().split())) for _ in range(size)]
result = 0

# 이동 함수 (상, 하, 좌 우)
# 인덱스 위치를 이동하면서 값이 같은지 체크하고, 같으면 더하고 다르면 그냥 냅두기
def move(direction):
    if direction == 0:  # 상
        for j in range(size):
            top = 0
            for i in range(1, size):
                if board[i][j]:
                    temp = board[i][j]  # 해당 값을 변수에 저장하고
                    board[i][j] = 0  # 그 자리의 값을 0으로 변경

                    if board[top][j] == 0:  # 이동하려는 자리의 값이 0이면
                        board[top][j] = temp  # 이전 자리의 값을 넣음
                    elif board[top][j] == temp:  # 이동하려는 자리의 값이 이전 자리의 값과 같은 경우
                        board[top][j] = temp * 2  # 이전 자리의 값에서 곱하기 2한 값을 넣음
                        top += 1
                    else:  # 이동하려는 자리의 값이 이전 자리의 값과 다르고 0이 아닌 경우
                        top += 1
                        board[top][j] = temp  # 원래 자리에다가 다시 넣음

    elif direction == 1:  # 하
        for j in range(size):
            top = size - 1  # 위에서 아래로 가는거니까 가장 큰 값에서 값을 하나씩 줄여나감
            for i in range(size - 2, -1, -1):  # 시작범위, 마지막범위, 이동 값
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = temp


    # 위, 아래와 다르게 배열 인덱스를 반대로 시작함
    elif direction == 2:  # 좌
        for i in range(size):
            index = 0
            for j in range(1, size):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[i][index] == 0:
                        board[i][index] = temp
                    elif board[i][index] == temp:
                        board[i][index] = temp * 2
                        index += 1
                    else:
                        index += 1
                        board[i][index] = temp

    elif direction == 3:  # 우
        for i in range(size):
            index = size - 1
            for j in range(size - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[i][index] == 0:
                        board[i][index] = temp
                    elif board[i][index] == temp:
                        board[i][index] = temp * 2
                        index -= 1
                    else:
                        index -= 1
                        board[i][index] = temp

# 이동 함수를 하나씩 호출하면서 모든 경우의 수를 탐색하는 함수 (재귀호출)
def dfs(count):
    global result, board
    if count == 5:
        for i in range(size):
            result = max(result, max(board[i]))
            return

    temp = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(count + 1)
        board = copy.deepcopy(temp)

dfs(0)
print(result)