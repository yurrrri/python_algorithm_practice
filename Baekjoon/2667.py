import sys

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
  board.append(list(map(int, sys.stdin.readline().rstrip())))
  
answer = 0

def dfs(x, y):
  global num
  
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return False

  if board[x][y] == 1:
    board[x][y] = 2 #방문처리
    num += 1
    
    dfs(x-1, y) #dx, dy와 반복문으로 대체 가능
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    
    return True
  return False

num = 0
temp = []

for i in range(n):
  for j in range(n):
    if dfs(i, j) == True: #집 구역
      temp.append(num)
      answer += 1
      num = 0

print(answer)
temp.sort()
for i in temp:
  print(i)