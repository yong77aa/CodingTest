def sol(count):
    result = 0

    for i in arr:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
result = sol(count)
print(result)