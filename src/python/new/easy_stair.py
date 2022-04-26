def cal(n, arr):
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                arr[i][j] = arr[i-1][1]
            elif j == 9:
                arr[i][j] = arr[i-1][8]
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

n = int(input())
arr = [[0] * 10 for _ in range(n)]
for i in range(1, 10):
    arr[0][i] = 1

cal(n, arr)
print("result: " + str(sum(arr[n-1]) % 1000000000))