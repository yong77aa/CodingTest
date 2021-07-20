def main():
    num = int(input())
    list = []
    result = 0

    for i in range(0, num):
        value = int(input())

        if value == 0:
            list.pop()
        else:
            list.append(value)

    for i in list:
        result += i

    print(result)


if __name__ == '__main__':
    main()
