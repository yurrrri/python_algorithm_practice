import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
board = []
total_wolf = 0
total_yang = 0

for i in range(r):
  board.append(list(input()))
  for j in range(c):
    if board[i][j] == "v":
      total_wolf += 1
    elif board[i][j] == "o":
      total_yang += 1
      
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global wolf
  global yang
  
  visited[x][y] = True
  if board[x][y] == "v":
    wolf += 1
  elif board[x][y] == "o":
    yang += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<r and 0<=ny<c and board[nx][ny] != "#" and not visited[nx][ny]:
      dfs(nx, ny)

visited = [[False] * c for _ in range(r)]
for i in range(r):
  for j in range(c):
    if not visited[i][j] and board[i][j] != "#":
      yang = 0
      wolf = 0
      dfs(i, j)

      if yang > wolf: # 양이 늑대보다 많으면 늑대를 우리에서 쫓아냄
        total_wolf -= wolf
      else:  # 그렇지 않다면 늑대가 양을 먹음
        total_yang -= yang

print(total_yang, total_wolf)