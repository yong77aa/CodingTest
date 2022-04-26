#  1번역부터 10번역까지
#  타거나 내리는 사람 수 자동인식
#  기차 안에 사람이 가장 많을 때
#  내린 사람이 모두 내린 이후에 탑승

def main():
    temp_train = 0  # 각 열차마다 사람수를 계산하기 위한 변수
    train = []  # 각 열차마다 사람수를 저장하기 위한 리스트

    for i in range(10):  # 10번 반복
        a, b = list(map(int, input().split()))  # 내린 사람 수, 탄 사람 수
        temp_train = temp_train - a + b  # 내린 사람 수만큼 빼고, 탄 사람 수만큼 더하기
        train.append(temp_train)  # 결과를 리스트에 누적

    print(max(train))  # 리스트의 가장 큰 수 (사람이 가장 많을 때)

if __name__ == "__main__":
    main()