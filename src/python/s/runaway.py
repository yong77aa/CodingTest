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
                diff = arr[j][i] - arr[j+1][i]  # 차이

                if diff == 1 and j+1+l <= n:
                    # 높은 경사에서 낮은 경사로 가는 경우
                    # 1. 낮은 칸과 높은 카의 차이가 1이 아닌 경우 확인
                    # 2. 범위 안에 들어가는 경우 확인
                    for k in range(j+1, j+1+l):
                        if check[k] == 1 or arr[k][i] != arr[j][i] - 1:
                            # 3. 경사로를 놓은 곳에 경사로를 또 놓는지 확인
                            # 4. 낮은 지점 칸의 높이가 모두 같지 않거나, 연속되지 않는지 확인
                            bool = False
                            break

                    if bool == False:
                        break

                    for k in range(j+1, j+1+l):
                        # 경사로 설치가 가능한 경우, 해당 위치는 설치한 것으로 수정
                        check[k] = 1

                elif diff == -1 and j+1-l >= 0:
                    # 낮은 경사에서 높은 경사로 가는 경우
                    # 1. 낮은 칸과 높은 카의 차이가 1이 아닌 경우 확인
                    # 2. 범위 안에 들어가는 경우 확인
                    for k in range(j+1-l, j+1):
                        if check[k] == 1 or arr[k][i] != (arr[j+1][i] - 1):
                            # 3. 경사로를 놓은 곳에 경사로를 또 놓는지 확인
                            # 4. 낮은 지점 칸의 높이가 모두 같지 않거나, 연속되지 않는지 확인
                            bool = False
                            break

                    if bool == False:
                        break

                    for k in range(j+1-l, j+1):
                        check[k] = 1

                else:
                    bool = False
                    break

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
                elif check[(j+1)-l] == 1 or arr[i][j+1] - arr[i][j+1-l] != 1 or j+1-l < 0:
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