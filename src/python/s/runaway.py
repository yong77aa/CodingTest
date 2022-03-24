n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0


for i in range(n):
    check = [0] * n  # 경사로 위치 저장
    bool = True

    for j in range(n-1):
        if abs(arr[j][i] - arr[j+1][i] >= 2):
            # 두 칸의 차이가 2인 경우
            bool = False
            break  # 지나갈 수 없음
        else:
            # 두 칸의 차이가 2가 나지 않는 경우
            if arr[j][i] == arr[j+1][i]:
                # 두 칸의 값이 같은 경우
                continue  # 계속 실행
            else:
                # 두 칸의 차이가 1인 경우 (경사로 설치)
                if arr[j][i] > arr[j+1][i]:
                    # 더 높은 경사에서 낮은 경사로 가는 경우
                    continue
                elif j-l < 0 or check[j-l] == 1 or arr[j-l][i] >= arr[j][i]:
                    # 경사로를 설치할 수가 없거나 이미 경사로가 설치된 경우
                    print("안되는 경우 i: " + str(i) + " j: " + str(j) + " l: " + str(l))
                    bool = False
                    break
                else:
                    # 경사로를 설치할 수 있는 경우
                    for k in range(j-l, j):
                        # 경사로 설치한 위치는 설치했다고 수정
                        check[k] == 1

    if bool:
        print("세로 가능: " + str(i) + " ")
        result += 1

for i in range(n):
    check = [0] * n  # 경사로 위치 저장
    bool = True

    for j in range(n-1):
        if abs(arr[i][j] - arr[i][j+1] >= 2):
            # 두 칸의 차이가 2인 경우
            bool = False
            break  # 지나갈 수 없음
        else:
            # 두 칸의 차이가 2가 나지 않는 경우
            if arr[i][j] == arr[i][j+1]:
                # 두 칸의 값이 같은 경우
                continue  # 계속 실행
            else:
                # 두 칸의 차이가 1인 경우 (경사로 설치)
                if arr[i][j] > arr[i][j+1]:
                    # 더 높은 경사에서 낮은 경사로 가는 경우
                    continue
                elif j-l<0 or check[j-l] == 1 or arr[i][j-l] >= arr[i][j]:
                    # 경사로를 설치할 수가 없거나 이미 경사로가 설치된 경우
                    bool = False
                    break
                else:
                    # 경사로를 설치할 수 있는 경우
                    for k in range(j-l, j):
                        # 경사로 설치한 위치는 설치했다고 수정
                        check[k] == 1

    if bool:
        print("가로 가능: " + str(i) + " ")
        result += 1

print(result)