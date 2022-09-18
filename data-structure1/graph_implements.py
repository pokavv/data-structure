from sys import stdin

# 구현 방법 두 가지 존재
    # 인접행렬을 통한 그래프 구현 adj[i][j]
        # 시간적으로 더 유리
node, edge = map(int, stdin.readline().split())
adj = [[0] for _ in range(node) for _ in range(node)]

for i in range(edge):
    src, dest = map(int, stdin.readline().split())
    adj[src][dest] = 1
    adj[dest][src] = 1

    # 인접리스트를 통한 그래프 구현
        # 공간적으로 더 유리