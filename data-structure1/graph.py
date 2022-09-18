# 방향
    # 방향그래프 : {0:{1}, 1:{1,2},3:{0}}
'''g = <v, e>
v(g) = {0, 1, 2, 3}
e(g) = {<0, 1>, <0, 2>, <1, 2>, <2, 3>, <3, 2>} # <x, y> : x가 head, y가 tail
max_e = n(n - 1)''' # 정점의 개수가 n인 경우, 최대 edge의 개수

    # 무방향그래프 : {0: {1,2}, 1: {0}, 2:{0,3}, 3:{2}}
'''g = (v, e)
v(g) = {0, 1, 2, 3}
e(g) = {(0, 1), (0, 2), (0, 3), (2, 3)}
max_e = n(n - 1) / 2''' # 정점의 개수가 n인 경우, 최대 edge의 개수

# 순환성
    # 순환 그래프
    # 비순환 그래프

# DAG : 방향성 비순환 그래프 ex. Version Control System
# Tree : 무방향 비순환 그래프
# 연결요소

# 인접리스트
k = 4
graph = {}

for i in range(k):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)
    if y not in graph.keys():
        graph[y] = set([x])
    else:
        graph[y].add(x)

print(graph)