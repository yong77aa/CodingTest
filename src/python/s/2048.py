# 같은 값을 만나면 합쳐짐
# 5번을 움직여서 가장 큰 수 (전체가 다 움직임)

from sys import stdin

size = stdin.readline()
# 현재 보드의 상태 저장
board = [list(stdin.readline()) for _ in range(size)]

