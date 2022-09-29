# f(n, d): 길이가 n이고 마지막 숫자가 d인 계단수 개수
import sys
input = sys.stdin.readline

val = 1_000_000_000
tmp = [[0] * 10 for _ in range(101)]
cnt = 0

for i in range(1, 10):
    tmp[1][i] = 1

for a in range(2, 101):
    for b in range(10):
        if b > 0:
            tmp[a][b] += tmp[a - 1][b - 1]
            tmp[a][b] % val
        if b < 9:
            tmp[a][b] += tmp[a - 1][b + 1]
            tmp[a][b] % val
        cnt += 1

res = 0
num = int(input())
for i in range(10):
    res += tmp[num][i]
    res %= val

print(res)
print(f'count: {cnt}')