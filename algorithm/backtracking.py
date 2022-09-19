# 백트래킹 Backtracking (퇴각검색)
# 기본적을 모든 경우를 탐색 > DFS / BFS와 방식은 유사
# 백트래킹은 가지치기를 통해 탐색 경우의 수를 줄인다는 차이가 있음
    # 최악의 경우, 모든 경우를 살펴보게 될 수도 있지만 가능한 덜 보겠다는 전략

# boj 11724 : (n(n-1)/2 : 자기자신 가르키는 행렬X)
# [1, 2, 5] 순환연결, [3, 4, 6] 연결
import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
adj = [[0] * node for _ in range(node)]
checking = [False] * node
res = 0

def dfs(now):
    for nxt in range(node):
        if adj[now][nxt] and not checking[nxt]:
            checking[nxt] = True
            dfs(nxt)

for _ in range(edge):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    adj[u][v] = adj[v][u] = 1 # 무방향 그래프

for i in range(node):
    if not checking[i]:
        res += 1
        checking[i] = True
        dfs(i)

print(res)