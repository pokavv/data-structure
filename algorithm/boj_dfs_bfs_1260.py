import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(start):
    dq = deque([start])
    visited[start] = True
    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

# n: 정점의 개수, m: 간선의 개수, start_v: 탐색 시작정점 위치
n, m, start_v = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)] # vertex 0은 없기에 graph[0] = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i].sort() # 작은 노드부터 방문필요 = sort()로 정렬

dfs(start_v)
print()
visited = [False] * (n + 1) # visited 초기화
bfs(start_v)