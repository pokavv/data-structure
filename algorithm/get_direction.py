# 길찾기 문제
# 방향값을 미리 코드에 짜두고 for문으로 순회
# 방문체크 필요, 각 칸이 노드, 상하좌우 4방향의 간선
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
checking = [[False] * 100 for _ in range(100)]
num = int(input())

def is_valid_coord(y, x):
    return 0 <= y < num and 0 <= x < num

def bfs(start_y, start_x):
    dq = deque()
    dq.append((start_y, start_x))
    while len(dq) > 0:
        y, x = dq.popleft()
        checking[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_coord(ny, nx) and not checking[ny][nx]:
                dq.append((ny, nx))