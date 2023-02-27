import sys
import heapq

INF = int(1e9)
q = []

n, m, start = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

def dijkstra(start):
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    #이미 처리한 것으로 보고 무시
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
      
print(count-1, max_distance)