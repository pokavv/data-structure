num, k = map(int, input().split())
coin = []
res = 0

for _ in range(num):
    coin.append(int(input()))
coin.reverse()

for i in coin:
    res += k // i
    k %= i

print(res)