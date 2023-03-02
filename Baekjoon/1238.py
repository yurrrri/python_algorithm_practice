import sys
import heapq

INF = int(1e9)
q = []
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  distance = [INF] * (n+1)
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance

result = 0

for i in range(1, n+1):
  go = dijkstra(i) 
  back = dijkstra(x)
  #go[x] : 집에서 x로 가는길
  #back[i] : x에서 i로 가는길
  result = max(result, go[x] + back[i])
print(result)