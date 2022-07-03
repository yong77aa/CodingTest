import sys

# sys.stdin = open("in1.txt", "rt")
target = input()
number = ''

for i in target:
    if i.isnumeric():
        number += i

number = int(number)
div = 0

for i in range(1, number+1):
    if number % i == 0:
        # 약수인 경우
        div += 1

print(number)
print(div)
