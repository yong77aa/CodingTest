import sys

# sys.stdin = open("in1.txt", "rt")

arr = [i+1 for i in range(20)]

for i in range(10):
    start, end = map(int, input().split())
    temp_arr = arr[start-1:end]
    reverse_arr = temp_arr[::-1]
    arr[start-1:end] = reverse_arr

print(*arr)
