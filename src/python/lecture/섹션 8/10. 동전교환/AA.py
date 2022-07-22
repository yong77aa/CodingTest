import sys
sys.stdin = open("in1.txt")

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dy = [1000] * (target+1)
    dy[0] = 0

    for i in range(n):
        coin_type = coins[i]
        for j in range(coin_type, target+1, coin_type):
            dy[j] = min(dy[j], dy[j-coin_type]+1)

    print(dy[target])




