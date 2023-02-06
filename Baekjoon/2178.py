import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
visited = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def bfs():
  global visited
  
  q = deque([[0, 0]])

  while q:
    x, y = q.popleft()
    visited.append([x, y])

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1 and [nx, ny] not in visited:
        board[nx][ny] = board[x][y] + 1
        q.append([nx, ny])

bfs()
print(board[n-1][m-1])