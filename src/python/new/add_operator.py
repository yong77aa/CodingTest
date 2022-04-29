def find(index, now):
    global n, arr, plus, minus, multiple, divide, max_value, min_value

    if index == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if plus > 0:
            plus = plus - 1
            find(index + 1, now + arr[index])
            plus = plus + 1
        elif minus > 0:
            minus = minus - 1
            find(index + 1, now - arr[index])
            minus = minus + 1
        elif multiple > 0:
            multiple = multiple - 1
            find(index + 1, now * arr[index])
            multiple = multiple + 1
        elif divide > 0:
            divide = divide - 1
            find(index + 1, int(now / arr[index]))
            divide = divide + 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plus, minus, multiple, divide = map(int, input().split())

    max_value = -1000000001
    min_value = 1000000001

    find(1, arr[0])

    print(max_value)
    print(min_value)

