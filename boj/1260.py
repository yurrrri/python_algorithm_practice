import sys
from collections import deque

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * (n+1) for i in range(n+1)]
visited = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    visited[x][y] = 1
    visited[y][x] = 1
    
dfs(graph, v, visited)
print()
bfs(graph, v, visited)