# 일곱 난쟁이의 키의 합이 100
# 아홉 개의 줄에 걸쳐 난쟁이들 키 출력

def main():
    dwarfs = []  # 키 저장 리스트
    total = 0  # 전체 총합

    a = 0  # 제외해야하는 첫번째 값
    b = 0  # 제외해야하는 두번째 값

    for i in range(9):
        # 입력받아서 리스트에 저장 및 총합 계산
        temp = int(input())
        dwarfs.append(temp)
        total += temp

    dwarfs.sort()

    for i in range(9):
        for j in range(i+1, 9):
            if total - (dwarfs[i] + dwarfs[j]) == 100:  # 7개중에 2개만 빠지면 되니까 2개 더한걸 총합에서 빼서 100인걸 찾음
                a, b = dwarfs[i], dwarfs[j]
                break

    # 해당 값 리스트에서 제외
    dwarfs.remove(a)
    dwarfs.remove(b)
    dwarfs.sort()

    for i in dwarfs:
        print(i)

if __name__ == '__main__':
    main()