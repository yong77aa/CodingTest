import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())

for i in range(n):
    temp = input().lower()
    reverse_temp = temp[::-1].lower()

    if temp == reverse_temp:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" % (i+1))