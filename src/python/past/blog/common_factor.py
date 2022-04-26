# 두개의 수 최대공약수, 최대공배수

def main():
    a, b = list(map(int, input().split()))

    greatest1 = a
    greatest2 = b

    while greatest2 > 0:

        if greatest2 == 0:
            print(greatest1)
            break

        greatest1 = greatest1 % greatest2
        greatest2 = greatest2 % greatest1

        if greatest2 == 0:
            print(greatest1)
            break

    smallest = a * b / greatest1
    print(int(smallest))

if __name__ == "__main__":
    main()