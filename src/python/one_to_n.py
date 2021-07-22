def main():
    target = int(input())

    addNum(1, target)

def addNum(value, target):
    print(value)
    value = value + 1

    if value <= target:
        addNum(value, target) # 재귀 호출

if __name__ == "__main__":
    main()
