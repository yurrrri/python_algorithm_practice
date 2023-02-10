import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())

list = [0]*(f+1)
visited = [0]*(f+1)

def bfs():
  global visited
  
  q = deque([s])
  visited[s] = 1

  while q:
    a = q.popleft()
    if a == g:
      break

    if a+u<=f and not visited[a+u]:
      q.append(a+u)
      visited[a+u] = visited[a]+1 

    if a-d>=1 and not visited[a-d]:
      q.append(a-d)
      visited[a-d] = visited[a]+1

bfs()

if visited[g] == 0:
  print("use the stairs")
else:
  print(visited[g]-1)