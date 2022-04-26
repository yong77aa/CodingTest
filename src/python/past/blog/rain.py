# 첫째줄에는 세로길이, 가로길이
# 두번째에는 높이
# 고이는 빗물의 총량

def main():
    max = 1

    H, W = map(int, input().split())  # 세로, 가로길이
    box = list(map(int, input().split()))  # 높이

    for i in range(len(box)):
        if max < box[i]:
            max = box[i]
            maxIndex = i

    total = 0
    value = 0

    for i in range(maxIndex + 1):
        if box[i] > value:
            value = box[i]
        total += value

    value = 0
    for i in range(W-1, maxIndex, -1):
        if box[i] > value:
            value = box[i]
        total += value

    print(total - sum(box))

if __name__ == '__main__':
    main()
