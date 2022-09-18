############################
# 비순환 무방향 그래프
# 특정하지 않는 한 어떤 node든지 root가 될 수 있음
# 가장 바깥 node는 leaf node
# node A에서 node B로 가는 경로는 무조건 존재하며 유일함
# node 개수 = edge 개수 + 1
# 자료구조에서의 tree는 부모-자식 관계가 있는 방향 그래프(root는 하나)
############################

class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = node(10)

root.left = node(34)
root.right = node(89)
root.left.left = node(45)
root.left.right = node(50)

print("""
            10
        34      89
    45      50
      """)

#################################

from anytree import Node, RenderTree

root = Node(10)

level_1_child_1 = Node(34, parent=root)
level_1_child_2 = Node(89, parent=root)
level_2_child_1 = Node(45, parent=level_1_child_1)
level_2_child_2 = Node(50, parent=level_1_child_2)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))