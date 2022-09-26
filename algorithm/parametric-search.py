'''
최적화문제를 결정문제로 바꿔서 품

- 최적화문제: 문제 상황을 만족하는 변수의 최소, 최댓값 구하는 문제
- 결정문제: YES / NO

1. 매개변수 Parameter가 주어지면 true or false가 결정되어야 함
2. 가능한 해의 영역이 연속적이어야 함
3. 범위를 반씩 줄여가면서 가운데 값이 true인지 false인지 구해야 함
4. 이진탐색과 똑같은 원리
'''

# boj 2512 예산

n = int(input())
req = list(map(int, input().split()))
m = int(input())

low = 0
high = max(req)
mid = (low + high) // 2
res = 0

def is_possible(mid):
    return sum(min(i, mid) for i in req) <= m

while low < high:
    print(f'low: {low}, mid: {mid}, high: {high}, res: {res}')
    if is_possible(mid):
        low = mid + 1
        res = mid
    else:
        high = mid - 1
    
    mid = (low + high) // 2

print(res)