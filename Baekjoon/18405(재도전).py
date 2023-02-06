#다시 풀어봐야함
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(n):
  board.append(list(map(int, sys.stdin.readline().rstrip().split())))

s, x, y = map(int, sys.stdin.readline().rstrip().split())
#s: s초 뒤, x, y: 찾을 좌표

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1] # 상하좌우

def dfs(virus):
  
  if virus > k:
    return
  
  for i in range(n):
    for j in range(n):
      if board[i][j] == virus:
        x, y = i, j

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
      board[nx][ny] = virus

  dfs(virus+1)

for _ in range(s):
  dfs(1)

print(board[x-1][y-1])