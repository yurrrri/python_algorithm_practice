import sys

input = sys.stdin.readline
n, k = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j:
      graph[i][j] = 0 

for _ in range(k):
  a, b = map(int, input().split())
  graph[a][b] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

s = int(input())

for _ in range(s):
  a, b = map(int, input().split())
  if graph[a][b] != INF: #a가 먼저 일어남
    print(-1)
  elif graph[b][a] != INF: #b가 먼저 일어남
    print(1)
  else:
    print(0)