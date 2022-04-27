def sol(n ,arr):
    for i in range(1, n):
        for j in range(0, 10):
            for k in range(j, 10):
                arr[i][j] += arr[i-1][k]


if __name__ == '__main__':
    n = int(input())
    arr = [[0] * 10 for i in range(n)]
    for i in range(0, 10):
         arr[0][i] = 1
    sol(n, arr)
    compare = 10007
    print(sum(arr[n-1]) % compare)
