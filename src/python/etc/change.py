pay = int(input())
money_list = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
money_list.sort(reverse=True)
result = 0

for i in money_list:
    temp = 0
    temp += pay // i
    pay = pay - (temp * i)

    result += temp
    if pay == 0:
        break

print(result)