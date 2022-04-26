def compare_value(arr):
    global count
    for i in arr:
        myList = list(str(i))

        result = True
        for index, val in enumerate(myList):
            if index < len(myList) - 1:
                if int(myList[index + 1]) - int(myList[index]) != 1:
                    result = False
                    break
        if result:
            # 계단
            count += 1


n = int(input())
arr = []
min = 10 ** (n-1)
max = 10 ** (n) - 1
count = 0

for i in range(min, max+1):
    arr.append(i)

compare_value(arr)
print(str(count % 1000000000))