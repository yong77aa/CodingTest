import heapq

def main():
    arr = list(map(int, input().split()))
    target = int(input())

    count = 0
    heapq.heapify(arr)

    while arr[0] < target:
        temp = heapq.heappop(arr) + (heapq.heappop(arr) * 2)
        heapq.heappush(arr, temp)
        count += 1

        if len(arr) == 1 and arr[0] < target:
            return -1

    if count == 0:
        return -1
    else:
        print(count)

if __name__ == '__main__':
    main()