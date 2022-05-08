def cal(value):
    result = 0
    for i in range(len(value) + 1):
        if int(value[i]) <= 1 or result <= 1:
            result += value[i]
        else:
            result *= value[i]

    return result


value = input()
result = cal(value)
print(result)