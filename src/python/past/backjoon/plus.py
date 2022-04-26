# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법
# 각 줄마다 목표 값이 입력됨
import sys

def solution(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return solution(num-1) + solution(num-2) + solution(num-3)

num = int(sys.stdin.readline())  # 목표 값 (한 줄 단위로 입력)

for _ in range(num):
    print(solution(int(sys.stdin.readline())))