'''
동적계획법 Dynamic Programming

문제를 쪼개서 작은 문제의 답을 구하고, 그것으로 더 큰 문제의 답을 구하는 걸 반복
분할정복과 유사
DP Table에 저장 후 이용

구현 방법
1. Top-down
- 구현: Recursion
- 저장 방식: Memoization

2. Bottom-up
- 구현: Loop
- 저장 방식: Tabulation

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

# 기존 방식 : input 40만 넘어가도 오래걸림

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(int(input())))

##################################################

# Memoization

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def fibo_memoi(n):
    if cache[n] == -1:
        cache[n] = fibo_memoi(n - 1) + fibo_memoi(n - 2)
    
    return cache[n]

print(fibo_memoi(int(input())))