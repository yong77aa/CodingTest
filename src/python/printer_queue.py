def main():
    num = int(input())

    for _ in range(num):
        size, index = list(map(int, input().split()))
        imp = list(map(int, input().split()))

        # 같은 크기를 가지는 리스트를 생성
        # 단순 sort만 하면 같은 숫자가 여러개 나왔을 때 몇번째 index인지를 구분할 수가 없음
        tmp = [0 for _ in range(size)]
        tmp[index] = 1 # 목표 인덱스를 1로 변경
        count = 0

        while imp:
            if imp[0] == max(imp): # 처음값이 최댓값(가장 높은 우선순위를 가지는)과 같으면
                count += 1 # 카운트를 하나 증가시키고
                if tmp[0] == 1: # 그 값이 목표값이면
                    print(count)
                    break # 종료
                else: # 그 값이 목표값과 같지 않으면
                    # 해당 값들을 뺌
                    tmp.pop(0)
                    imp.pop(0)
            else: # 처음값이 최댓값이 아니면
                # 첫번째 값을 맨 뒤로 보내고
                imp.append(imp[0])
                tmp.append(tmp[0])
                # 삭제
                del(imp[0])
                del(tmp[0])

if __name__ == '__main__':
    main()
