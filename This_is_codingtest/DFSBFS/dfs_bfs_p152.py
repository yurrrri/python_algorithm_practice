from collections import dequeue
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(n):
  board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
  
def bfs():
  queue = dequeue([0, 0])
  x = 0
  y = 0
  count = 1

  while !queue.isEmpty:
    a = queue.popleft()

    for i in range(4): # 4방향 모두 검토
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue

      if board[nx][ny] == 0: #괴물일 때는 피해감
        continue
      else:
        count += 1
        board[nx][ny] = count
        queue.append([nx, ny])

  return board[n-1][m-1]


print(bfs())
  