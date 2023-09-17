from collections import deque

n, k = map(int, input().split())   # k 이하의 자연수로만 바이러스 번호가 이루어져있음
viruses = []
board = []
for i in range(n):
  read = list(map(int, input().split()))
  board.append(read)
  for j in range(n):
    if board[i][j] != 0:
      viruses.append((board[i][j], 0, i, j))

s, x, y = map(int, input().split())  # s초 뒤에 x-1, y-1 위치에 있는 바이러스 종류를 출력하면됨
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

viruses.sort()  # 번호가 낮은 종류의 바이러스부터 먼저 증식

def bfs():
  q = deque(viruses)

  while q:
    virus, time, x, y = q.popleft()   # 번호가 낮은 종류 바이러스 순서대로 뽑혀서 증식하게됨

    if time == s:
      break
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
        board[nx][ny] = virus
        q.append((virus, time+1, nx, ny))

bfs()
print(board[x-1][y-1])import sys

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