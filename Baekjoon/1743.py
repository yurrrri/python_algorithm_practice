import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
for _ in range(k):
  a, b = map(int, input().split())
  board[a-1][b-1] = 1 # 음쓰
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
answer = 0

def dfs(x, y):
  global count
  
  visited[x][y] = True
  count += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 1:
      dfs(nx, ny)
        
  return count

for i in range(n):
  for j in range(m):
    if not visited[i][j] and board[i][j] == 1:
      count = 0
      answer = max(answer, dfs(i, j))

print(answer)