#############
# 삽입/삭제: O(1)
# FIFO (First In First Out)
#############

from collections import deque

q = deque() # deque: 양방향 큐(double-ended queue)
q.append(123)
q.append(456)
q.append(789)
print('size: ', len(q))

while len(q) > 0:
    print(q.popleft())

###########################################

from queue import Queue

qu = Queue() # 멀티스레드에서 안정성은 증가하지만 시간이 더 소요
qu.put(123)
qu.put(456)
qu.put(789)

while qu:
    print(qu.get())