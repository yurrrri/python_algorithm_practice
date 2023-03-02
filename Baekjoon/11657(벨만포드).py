import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
q = []

n, m = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        cost = distance[i[0]]
        heapq.heappush(q, (cost, i[0]]))

dijkstra(1)

for i in range(1, n+1):
  if distance[i] < 0:
    print(-1)
    exit(0)

for i in range(1, n+1):
  if distance[i] == INF:
    print(-1)
  else:
    print(distance[i])