# Depth First Search 깊이우선탐색
# Stack or Recursive(재귀) 이용

adj = [[0] * 13 for _ in range(13)]

for row in adj:
    print(row)
    
def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)

dfs(0)