import sys
import heapq
input = sys.stdin.readline
pq = []

for i in range(int(input())): # 연산 개수 지정
    x = int(input()) # 정수 x 입력
    if x: # 만약 x가 0이 아니면
        heapq.heappush(pq, (abs(x), x)) # pq에 (절대값x와 x값) heappush
    else: # 만약 x가 0이면
        if pq: # 만약 pq에 값이 있으면
            print(heapq.heappop(pq)[1]) # pq에서 가장 작은 값 heappop(가장 작은 요소 pop)
        else:
            print(0)