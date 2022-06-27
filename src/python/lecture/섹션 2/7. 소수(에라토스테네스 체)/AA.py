import sys
import math

# sys.stdin = open("in2.txt", "rt")
n = int(input())
result = 0


def is_prime_number(target):
    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i == 0:
            # 나누어 떨어지는 경우 소수가 아님
            return False
    # 나누어 떨어지지 않는 경우 소수
    return True


for i in range(2, n+1):
    if is_prime_number(i):
        # 나누어 떨어지지 않는 경우
        result += 1

print(result)