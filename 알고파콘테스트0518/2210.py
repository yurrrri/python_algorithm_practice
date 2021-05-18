import sys

result = []

def dfs(x,y,v):
  if len(v)==6: #여기서 종료
    if v not in result:
      result.append(v)
    return

  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=5 or ny<0 or ny>=5:
      continue
    else:
      dfs(nx,ny,number+board[nx][ny])

board=[]
for i in range(5):
  board.append(list(map(str, sys.stdin.readline().rstrip().split())))

for i in range(5):
  for j in range(5):
    dfs(i,j,board[i][j])
print(len(result))