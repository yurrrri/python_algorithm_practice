# 나중에 풀어볼것
import sys

r, c, t = map(int, sys.stdin.readline().split())
board = []

for _ in range(r):
  board.append(list(map(int, sys.stdin.readline().split())))

for _ in range(t):
  for i in range(r):
    for j in range(c):
      count = 0 # 확산된 방향의 갯수
      
      if board[i][j] != 0:
        if board[i-1][j] != -1 and i-1>=0:
          board[i-1][j] += board[i][j]//5
          count += 1
        if board[i][j-1] !+ -1 and j-1>=0:
          board[i-1][j] += board[i][j]//5
          count += 1