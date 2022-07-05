import sys

# sys.stdin = open("in1.txt", "rt")

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

total_arr = arr1 + arr2
total_arr.sort()
print(*total_arr)