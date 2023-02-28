import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)] #2차원 배열

for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j:
      graph[i][j] = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a][b] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF: #서로 도달 가능
      count += 1

  if count == n:
    result += 1

print(result)