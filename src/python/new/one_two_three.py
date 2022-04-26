#  dp(dynamic programming)

def dfs(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return dfs(num-1) + dfs(num-2) + dfs(num-3)


n = int(input())  # 테스트케이스 개수
for i in range(n):
    a = int(input())
    print(dfs(a))