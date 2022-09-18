# Depth First Search 깊이우선탐색
# Stack or Recursive(재귀) 이용
import pprint

# list
visited = [False] * 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
pprint.pprint(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            print(i)

dfs(graph, 1, visited)

# source: https://daekyoulibrary.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%86%B5%ED%95%B4-%EA%B5%AC%ED%98%84%ED%95%9C-DFS%EC%99%80-BFS