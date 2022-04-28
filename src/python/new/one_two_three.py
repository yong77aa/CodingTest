def sol(val):
    if val == 1:
        return 1
    elif val == 2:
        return 2
    elif val == 3:
        return 4
    else:
        return sol(val-3) + sol(val-2) + sol(val-1)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        target = int(input())
        result = sol(target)
        print(result)