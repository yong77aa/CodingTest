def main():
    k = int(input())
    a = []
    result = 0

    for i in range(0, k):
        num = int(input())

        if num == 0:
            a.pop()

        else:
            a.append(num)

    for temp in a:
        result += temp

    print(result)

if __name__ == '__main__':
    main()