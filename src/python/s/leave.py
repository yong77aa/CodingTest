n = int(input())  # 남은 일수 N
arr = [list(map(int, input().split())) for _ in range(n)]
total_pay = 0  # 수익

index = 0  # 상담 종료일
total = 0  # 수익

for i, val in enumerate(arr):
    if i == 0 or i == index:
        index = val[0] + i  # 상담 종료일 저장
        if index > n:
            # 상담 종료일이 퇴사일보다 길어지는 경우
            break
        else:
            # 상담 종료일이 퇴사일보다 안쪽인 경우
            total += val[1]
    else:
        # 상담 종료일이 아닌 경우
        continue

print(total)