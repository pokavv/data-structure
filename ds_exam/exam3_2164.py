import sys
from collections import deque

num = int(sys.stdin.readline())
qlist = deque()

# qlist num 값에 따라 생성 [1, 2, 3, ---, num]
for i in range(num):
    qlist.append(i + 1)

# qlist가 최후의 1개보다 더 있을 때까지 반복
while len(qlist) > 1:
    qlist.popleft() # 맨 위 카드 버리기(pop)
    qlist.append(qlist.popleft()) # 맨 위 카드를 버린 후(popleft), 해당 pop return값을 맨 뒤로

print(qlist.pop()) # 최후의 qlist 요소 print