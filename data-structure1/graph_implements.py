import pprint

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 구현 방법 두 가지 존재
    # 인접행렬을 통한 그래프 구현 adj[i][j]
        # 시간적으로 더 유리
adj = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]

    adj[n1][n2] = 1 # n1과 n2 인접
    adj[n2][n1] = 1 # 방향 표시가 없는 경우

print('인접 행렬')
pprint.pprint(adj)
print()

    # 인접리스트를 통한 그래프 구현
        # 공간적으로 더 유리
adjList = [[] for _ in range(V + 1)]

for i in range(E):
    n1,n2 = arr[i * 2], arr[i * 2 + 1]
    
    adjList[n1].append(n2)
    adjList[n2].append(n1)
    
print('인접 리스트')
pprint.pprint(adjList)