###################
# 삽입/삭제: O(log N)
# data 추가는 어떤 순서로 해도 상관없지만, 제거될 때 가장 작은 값을 제거하는 특성
# >> 내부적으로 데이터를 정렬된 상태로 보관하는 매커니즘
# 이진트리 (root node 존재)
# C++: max-heap, Python: min-heap
# FIFO (First In First Out)
###################

import heapq

pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)
print('size: ', len(pq))

while len(pq) > 0:
    print(heapq.heappop(pq))

print()
#######################################

from queue import PriorityQueue

pqu = PriorityQueue() # 멀티스레드에서 안정성은 증가하지만 시간이 더 소요
pqu.put(6)
pqu.put(10)
pqu.put(-5)
pqu.put(0)
pqu.put(8)

while not pqu.empty():
    print(pqu.get()) # pop()