import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
  #기존과 달리 c를 바로 넣지 않고 최소값을 비교하는 이유? -> 시작도시와 도착도시를 연결하는 노선이 하나가 아니므로, 기존의 값과 새로 들어온 값을 비교해야함

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()