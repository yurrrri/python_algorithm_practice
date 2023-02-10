import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

def bfs(x, y):
  global con_pos
  global fes_pos
  global n
  
  q = deque([[x, y]])
  visited = [[x, y]]
  
  while q:
    a, b = q.popleft()

    if abs(a-fes_pos[0])+abs(b-fes_pos[1]) <= 1000:
      print("happy")
      return

    for i in range(n):
      if abs(a-con_pos[i][0])+abs(b-con_pos[i][1]) <= 1000 and [con_pos[i][0], con_pos[i][1]] not in visited:
        q.append([con_pos[i][0], con_pos[i][1]])
        visited.append([con_pos[i][0], con_pos[i][1]])
  print("sad")
  return

for _ in range(t):
  n = int(sys.stdin.readline().rstrip())
  house_pos = list(map(int, sys.stdin.readline().rstrip().split()))
  con_pos = []
  
  for _ in range(n):
    con_pos.append(list(map(int, sys.stdin.readline().rstrip().split())))
  fes_pos = list(map(int, sys.stdin.readline().rstrip().split()))
  bfs(house_pos[0], house_pos[1])
