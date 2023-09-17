import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  board.append(list(map(int, input().rstrip().split())))

def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = True  # 처음 들어오는 애 visited 처리 반드시 해주기
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] != 0 and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True
        elif board[nx][ny] == 0:
          count[x][y] += 1

  return 1  # 구역의 수

time = 0
while True:
  visited = [[False] * m for _ in range(n)] #탐색 할때마다 visited 초기화
  count = [[0] * m for _ in range(n)] #탐색 할때마다 초기화
  ans = 0
  
  for i in range(n):
    for j in range(m):
      if board[i][j] != 0 and not visited[i][j]: # 구역을 찾기 위해 탐색할때 visited = True 처리해주고, 아직 visited가 안되었을 때를 구역으로 count해야함
        ans += bfs(i, j)

  if ans == 0:
    print(0)
    break
  elif ans >= 2: #구역이 2개 이상으로 나뉘어짐 --> time 출력하고 break
    print(time)
    break

  for i in range(n):   # 빙산 녹이기
    for j in range(m):
      board[i][j] -= count[i][j]
      if board[i][j] < 0:
        board[i][j] = 0

  time += 1