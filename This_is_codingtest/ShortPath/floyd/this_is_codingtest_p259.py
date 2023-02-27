import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): #자기 자신은 0으로 초기화
  for j in range(1, n+1):
    if i==j:
      graph[i][j] = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a][b] = 1 #두 도시 사이의 거리는 1
  graph[b][a] = 1 #양방향

x, k = map(int, sys.stdin.readline().rstrip().split())

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print("-1")
else:
  print(distance)