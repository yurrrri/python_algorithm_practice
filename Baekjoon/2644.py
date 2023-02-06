import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
x, y = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
path = [0] * (n+1)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  q = deque([v])
  visited[v] = True

  while q:
    a = q.popleft()
    
    for i in graph[a]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        path[i] = path[a] + 1 #이전 노드와의 거리 계산

bfs(x)
print(path[y] if path[y]>0 else -1) #python 3항연산자 활용