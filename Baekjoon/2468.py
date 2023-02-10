import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())
board = []
min_high = 1e9
max_high = 1

for _ in range(n):
  a = list(map(int, sys.stdin.readline().rstrip().split()))
  board.append(a)
  min_high = min(min_high, min(a)) #보드의 최소값, 최대값 찾기
  max_high = max(max_high, max(a))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

num = 0

def dfs(x, y, high):
  global temp
  
  if x<0 or x>=n or y<0 or y>=n:
    return False

  if temp[x][y] > high:
    temp[x][y] = high-1
    
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      dfs(nx, ny, high)
    return True
  return False


temp = [[0] * n for _ in range(n)]
arr = []

for k in range(min_high, max_high+1):
  for i in range(n):
    for j in range(n):
      temp[i][j] = board[i][j] #그때그때 복사
  for i in range(n):
    for j in range(n):
      if dfs(i, j, k) == True:
        num += 1
  arr.append(num)
  num = 0

print(max(arr) if max(arr)>0 else 1)