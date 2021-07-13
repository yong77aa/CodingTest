def solution(numbers, target):
    a = [0]

    for i in numbers:
        b = []
        for j in a:
            # 더하고 뺀 것을 모두 list에 넣음
            b.append(j+i)
            b.append(j-i)
        a = b

    return a.count(target) # 리스트에서 target과 일치하는 것의 개수를 반환

def main():
    target = int(input())
    numbers = list(map(int, input().split()))

    answer = solution(numbers, target)
    print(answer)

if __name__ == '__main__':
    main()