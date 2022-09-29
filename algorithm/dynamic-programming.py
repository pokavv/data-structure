'''
동적계획법 Dynamic Programming

문제를 쪼개서 작은 문제의 답을 구하고, 그것으로 더 큰 문제의 답을 구하는 걸 반복
분할정복과 유사
DP Table에 저장 후 이용
점화식 찾고 Table을 잘 정의하기가 포인트

구현 방법
1. Top-down
- 구현: Recursion
- 저장 방식: Memoization
- 직관적이라 코드 가독성이 좋음
- 재귀함수 호출이 많아 느릴 수 있음

2. Bottom-up
- 구현: Loop
- 저장 방식: Tabulation
- 시간과 메모리를 더 아낄 수 있음
- DP Table을 채워 나가는 순서를 알아야 함

저장방식
1. Memoization
- 부분 문제의 답을 한번 구했으면 중복연산을 방지하기 위해 cache에 저장해두고 가져다 쓰기
- 필요한 부분 문제들만 구함 Lazy-Evaluation
- Top-down 방식에서 사용

2. Tabluation
- 부분 문제들의 답을 미리 전부 구하기
- 필요없는 문제들의 답도 모두 구함
- Bottom-up 방식에서 사용
'''
# boj 2748: 피보나치 수 2
# 피보나치 수열: f(n + 2) = f(n + 1) + f(n)
import sys
input = sys.stdin.readline

print('     피보나치 수열       ')
print()

# 기존 재귀 방식 : input 40만 넘어가도 오래걸림
cnt = 0

def fibo(n):
    global cnt
    cnt += 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(int(input())))
print(f'count: {cnt}')

# Memoization

cache = [-1] * 91
cache[0] = 0
cache[1] = 1
cnt_memoi = 0

def fibo_memoi(n):
    global cnt_memoi
    cnt_memoi += 1
    
    if cache[n] == -1:
        cache[n] = fibo_memoi(n - 1) + fibo_memoi(n - 2)
    
    return cache[n]

print(fibo_memoi(int(input())))
print(f'count: {cnt_memoi}')

# Tabulation

n_tabul = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1
cnt_tabul = 0

for i in range(2, n_tabul + 1):
    cache[i] = cache[i - 1] + cache[i - 2]
    cnt_tabul += 1

print(cache[n_tabul])
print(f'count: {cnt_tabul}')