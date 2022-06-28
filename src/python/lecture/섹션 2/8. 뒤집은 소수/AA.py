import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())
arr = list(map(str, input().split()))

# 문자열 뒤집기
def reverse(x):
    reverse_x = x[::-1]
    int_x = int(reverse_x)
    return int_x

# 소수 찾기
def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            # 소수아님
            return False
    # 소수
    return True

for i in arr:
    if isPrime(reverse(i)):
        print(reverse(i))

