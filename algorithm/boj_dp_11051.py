# boj 11051: 이항 계수 2
# 이항계수(nCr): bino(n, r) = bino(n - 1, r - 1) + bino(n - 1, r)
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
val = 10007
print('binomial coefficient')
print()

# 기존 재귀 방식

cnt = 0
n, k = map(int, input().split())

def binomial(n, k):
    global cnt
    
    if k == 0 or k == n:
        return 1
    cnt += 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

print(binomial(n, k))
print(f'count: {cnt}')

# Memoization

cnt_memoi = 0
cache = [[0] * 1001 for _ in range(1001)]
n_memoi, k_memoi = map(int, input().split())

def binomial_memoi(n, k):
    global cnt_memoi
    
    if cache[n][k]:
        return cache[n][k]
    
    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = binomial_memoi(n - 1, k - 1) + binomial_memoi(n - 1, k)
        cache[n][k] %= val # 10007로 나눈 나머지 구하기
    
    cnt_memoi += 1
    return cache[n][k]

print(binomial_memoi(n_memoi, k_memoi))
print(f'count: {cnt_memoi}')

# Tabulation

cnt_tabul = 0
cache = [[0] * 1001 for _ in range(1001)]
n_tabul, k_tabul = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
        cache[i][j] %= val
        cnt_tabul += 1

print(cache[n_tabul][k_tabul])
print(f'count: {cnt_tabul}')