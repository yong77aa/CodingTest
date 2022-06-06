# import sys
# sys.stdin = open("in1.txt", "rt")

case = int(input())

for i in range(case):
    n, s, e, k = map(int, input().split())

    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()

    print("#%d %d" %(i+1, arr[k-1]))
