# boj 2178
from collections import deque
import sys

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
n, m = map(int, sys.stdin.readline().split())
board = [input() for i in range(n)]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs():
    checking = [[False] * m for j in range(n)]
    checking[0][0] = True
    dq = deque(())
    dq.append((0, 0, 1))
    
    while dq:
        y, x, d = dq.popleft()
        nd = d + 1
        if y == n - 1 and x == m - 1:
            return d
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not checking[ny][nx]:
                checking[ny][nx] = True
                dq.append((ny, nx, nd))

print(bfs())