import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) #세로 크기 n, 가로크기 m
board = []
temp = [[0]*m for _ in range(n)]
position_list = []

for _ in range(n):
  board.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_safe = 0 #최대값

dx = [0, 0, 1, -1] #차례대로 동, 서, 남, 북
dy = [1, -1, 0, 0]

def virus(x, y): #바이러스 확산 함수
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx, ny)

def countSafe(board): #안전영역 세고, 최대값 도출하는 함수
  global max_safe
  count = 0
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        count += 1
  max_safe = max(max_safe, count)
    
def bfs(): #BFS
  for i in range(n):
    for j in range(m):
      temp[i][j] = board[i][j] # 복사

  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        virus(i, j)

  countSafe(temp)

a = 0
for i in range(n): #벽 세우기
  for j in range(m):
      if board[i][j] == 0:
        board[i][j] = 1
        a += 1
      
      if a == 3:
        bfs()
        board[i][j] = 0
        a -= 1
      
print(max_safe)