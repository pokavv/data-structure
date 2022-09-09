################
# 삽입/삭제: O(1) (array와 반대)
# 탐색: O(N)
# 다른 자료구조들을 구현할 떄 많이 쓰임
################

# Node 정의
class Node:
    def __init__(self, data, next=None): # data만 입력 시 next 초기값은 None.
        self.data = data # 다음 data 주소 초기값 = None
        self.next = next

# Node 생성(data = 1)
node_1 = Node(1)
node_2 = Node(3)

# Node의 값과 포인터 출력
print(node_1.data)
print(node_1.next)

# Node 연결
node_1.next = node_2

# 가장 맨 앞 Node를 알기 위해 head 지정
head = node_1

# node_1을 통해 연결한 결과 확인
print(node_1.next.data)
print(node_2.data)