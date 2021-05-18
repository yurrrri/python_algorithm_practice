import sys
from collections import deque

def dfs(graph, v, visited):
  visited[v] = 1
  print(v, end=' ')

  for i in graph[v]:
    if visited[i]==0:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = 1

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1


n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, .split())
    visited[x][y] = 1
    visited[y][x] = 1
    
dfs(graph, v, visited)
print()
bfs(graph, v, visited)